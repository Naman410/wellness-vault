"""
Setup all AnythingLLM workspaces for The Wellness Vault.

This script:
  1. Converts CSV files to readable TXT (AnythingLLM embeds TXT better)
  2. Uploads all sample data files to AnythingLLM staging
  3. Embeds files into the correct workspace
  4. Sets custom system prompts per workspace
  5. Sets all workspaces to RAG (query) mode
  6. Verifies each workspace with a test query

Prerequisites:
  - Ollama running (ollama serve)
  - AnythingLLM running
  - .env configured with ANYTHINGLLM_API_KEY
  - Sample data generated (run generate_sample_data.py first)

Usage: python execution/setup_workspaces.py
"""

import os
import csv
import sys
import time
import requests
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("ANYTHINGLLM_BASE_URL", "http://localhost:3001")
API_KEY = os.getenv("ANYTHINGLLM_API_KEY", "")
SAMPLE_DIR = Path(os.getenv("SAMPLE_DATA_DIR", ".tmp/sample_data"))

API = f"{BASE_URL}/api/v1"
HEADERS = {"Authorization": f"Bearer {API_KEY}"}
JSON_HEADERS = {**HEADERS, "Content-Type": "application/json"}

# ─────────────────────────────────────────────
# WORKSPACE CONFIGURATION
# ─────────────────────────────────────────────

WORKSPACES = {
    "customer-voice": {
        "source_dir": "customer_voice",
        "chat_mode": "query",
        "similarity_threshold": 0.25,
        "prompt": """You are a Customer Insights Analyst for a D2C wellness supplement brand. Your job is to analyze customer reviews, support tickets, and social media feedback to surface actionable insights.

When answering questions about customer feedback, always:

1. Cite specific reviews or tickets when possible (quote the relevant text).
2. Quantify patterns when you can (e.g., "7 out of 50 reviews mention this").
3. Separate facts from interpretations - state what the data says, then offer your analysis.
4. Flag when sample sizes are too small to draw reliable conclusions.
5. Suggest follow-up questions the team should investigate.

Output format: Start with a brief summary (2-3 sentences), then provide supporting details with specific examples. End with recommended next steps.

Important: You are an internal research tool. Your outputs will always be reviewed by a human before any decisions are made. If you're unsure about something, say so clearly."""
    },
    "team-brain": {
        "source_dir": "team_brain",
        "chat_mode": "query",
        "similarity_threshold": 0.25,
        "prompt": """You are the internal knowledge assistant for NovaBotanics. You have access to the company's SOPs, brand guidelines, meeting notes, and product documentation.

When answering questions:

1. Always reference which specific document your answer comes from.
2. If the answer isn't in the documents, say "I don't have this information in my current documents" - never make something up.
3. For process questions, provide step-by-step answers when the SOP supports it.
4. For historical questions ("why did we decide X?"), reference the relevant meeting notes or decision documents.
5. Keep answers concise but complete.

You are a search and retrieval tool, not a decision-maker. Always defer to the actual documents and the humans who wrote them."""
    },
    "competitor-intel": {
        "source_dir": "competitor_intel",
        "chat_mode": "query",
        "similarity_threshold": 0.25,
        "prompt": """You are a Competitive Intelligence Analyst for a D2C wellness supplement brand. You analyze competitor products, pricing, positioning, and market trends.

When answering:

1. Be specific - reference actual competitor names, ingredients, prices from the documents.
2. Always compare back to our products when relevant.
3. Identify gaps and opportunities, not just descriptions.
4. Flag when data might be outdated (check document dates).
5. Present findings in a structured format: Findings > Implications > Recommended Actions.

This is strategic analysis for internal use only. Your outputs inform decisions but do not make them."""
    },
    "supplier-intel": {
        "source_dir": "supplier_intel",
        "chat_mode": "query",
        "similarity_threshold": 0.25,
        "prompt": """You are a Supply Chain Analyst for a D2C wellness supplement brand. You analyze supplier documentation including Certificates of Analysis (COAs), pricing sheets, and correspondence.

When answering:

1. Reference specific suppliers, prices, and test results from the documents.
2. For comparison questions, present data in a clear format showing each supplier side by side.
3. Flag any quality concerns (e.g., heavy metal levels close to limits, missing certifications).
4. Note lead times and MOQ constraints that affect procurement decisions.
5. Always specify the date of the data you're referencing.

This tool assists procurement research. All purchasing decisions require human approval and direct supplier verification."""
    }
}

# Test questions per workspace (used for verification)
TEST_QUESTIONS = {
    "customer-voice": "What are the most common complaints about sleep gummies?",
    "team-brain": "Why did we reformulate the sleep gummies?",
    "competitor-intel": "How does our sleep gummy compare to ZenLeaf?",
    "supplier-intel": "Compare PurePlant and GreenSource on price and lead time."
}

# ─────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────

def check_prerequisites():
    """Verify Ollama and AnythingLLM are running, API key is set."""
    if not API_KEY:
        print("ERROR: ANYTHINGLLM_API_KEY not set in .env")
        sys.exit(1)

    # Check AnythingLLM
    try:
        r = requests.get(f"{API}/auth", headers=HEADERS, timeout=5)
        if not r.json().get("authenticated"):
            print("ERROR: AnythingLLM API key is invalid")
            sys.exit(1)
    except requests.ConnectionError:
        print("ERROR: AnythingLLM not running at", BASE_URL)
        sys.exit(1)

    # Check Ollama
    ollama_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    try:
        r = requests.get(f"{ollama_url}/api/tags", timeout=5)
        models = [m["name"] for m in r.json().get("models", [])]
        print(f"  Ollama models: {', '.join(models)}")
        if not any("embed" in m for m in models):
            print("  WARNING: No embedding model found. Run: ollama pull nomic-embed-text")
    except requests.ConnectionError:
        print("ERROR: Ollama not running at", ollama_url)
        sys.exit(1)

    print("  Prerequisites OK\n")


def csv_to_txt(csv_path):
    """Convert a CSV file to a readable TXT format for better RAG embedding."""
    txt_path = csv_path.with_suffix(".txt")
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames
        rows = list(reader)

    lines = []
    lines.append(f"Data from: {csv_path.name}")
    lines.append(f"Total records: {len(rows)}")
    lines.append("=" * 60)
    lines.append("")

    for i, row in enumerate(rows, 1):
        lines.append(f"--- Record {i} ---")
        for h in headers:
            val = row.get(h, "").strip()
            if val:
                lines.append(f"  {h}: {val}")
        lines.append("")

    with open(txt_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    return txt_path


def upload_file(file_path):
    """Upload a file to AnythingLLM staging. Returns the document path for embedding."""
    with open(file_path, "rb") as f:
        r = requests.post(
            f"{API}/document/upload",
            headers=HEADERS,
            files={"file": (file_path.name, f)}
        )

    data = r.json()
    if not data.get("success"):
        print(f"    FAILED to upload {file_path.name}: {data.get('error')}")
        return None

    doc = data["documents"][0]
    # Extract relative path from the full location
    loc = doc["location"]
    idx = loc.find("custom-documents")
    rel_path = loc[idx:].replace("\\", "/")
    print(f"    Uploaded: {file_path.name} ({doc['token_count_estimate']} tokens)")
    return rel_path


def embed_documents(workspace_slug, doc_paths):
    """Embed uploaded documents into a workspace one-by-one for reliability."""
    total = 0
    for doc_path in doc_paths:
        r = requests.post(
            f"{API}/workspace/{workspace_slug}/update-embeddings",
            headers=JSON_HEADERS,
            json={"adds": [doc_path], "deletes": []},
            timeout=120
        )
        data = r.json()
        count = len(data.get("workspace", {}).get("documents", []))
        if count > total:
            total = count
        time.sleep(1)  # small delay between embeddings
    return total


def update_workspace(workspace_slug, settings):
    """Update workspace settings (system prompt, chat mode, etc.)."""
    r = requests.post(
        f"{API}/workspace/{workspace_slug}/update",
        headers=JSON_HEADERS,
        json=settings
    )
    return r.json()


def clear_workspace(workspace_slug):
    """Remove all existing documents from a workspace before re-embedding."""
    r = requests.get(f"{API}/workspace/{workspace_slug}", headers=HEADERS)
    data = r.json()
    ws_list = data.get("workspace", [])
    if not ws_list:
        return

    ws = ws_list[0] if isinstance(ws_list, list) else ws_list
    docs = ws.get("documents", [])
    if docs:
        del_paths = [d["docpath"] for d in docs]
        requests.post(
            f"{API}/workspace/{workspace_slug}/update-embeddings",
            headers=JSON_HEADERS,
            json={"adds": [], "deletes": del_paths}
        )
        print(f"    Cleared {len(del_paths)} existing document(s)")


def test_query(workspace_slug, question):
    """Send a test query and return the response summary."""
    r = requests.post(
        f"{API}/workspace/{workspace_slug}/chat",
        headers=JSON_HEADERS,
        json={"message": question, "mode": "query"},
        timeout=300
    )
    data = r.json()
    sources = len(data.get("sources", []))
    response = data.get("textResponse", "")
    return response, sources


# ─────────────────────────────────────────────
# MAIN PIPELINE
# ─────────────────────────────────────────────

def main():
    print("=" * 60)
    print("THE WELLNESS VAULT - Workspace Setup")
    print("=" * 60)

    # Step 0: Check prerequisites
    print("\n[Step 0] Checking prerequisites...")
    check_prerequisites()

    # Step 1: Convert CSVs to TXT
    print("[Step 1] Converting CSV files to TXT for better RAG embedding...")
    csv_files = list(SAMPLE_DIR.rglob("*.csv"))
    converted_files = []
    for csv_file in csv_files:
        txt_file = csv_to_txt(csv_file)
        converted_files.append(txt_file)
        print(f"  Converted: {csv_file.name} -> {txt_file.name}")
    print()

    # Step 2-4: For each workspace: upload, embed, configure
    for ws_slug, config in WORKSPACES.items():
        print(f"[Setting up: {ws_slug}]")
        source_dir = SAMPLE_DIR / config["source_dir"]

        if not source_dir.exists():
            print(f"  ERROR: Source directory not found: {source_dir}")
            continue

        # Clear existing documents
        clear_workspace(ws_slug)

        # Collect TXT files only (CSVs have been converted)
        files_to_upload = list(source_dir.glob("*.txt"))
        if not files_to_upload:
            print(f"  WARNING: No .txt files found in {source_dir}")
            continue

        # Upload files
        print(f"  Uploading {len(files_to_upload)} files...")
        doc_paths = []
        for f in files_to_upload:
            path = upload_file(f)
            if path:
                doc_paths.append(path)

        # Embed into workspace
        if doc_paths:
            print(f"  Embedding {len(doc_paths)} files into workspace...")
            count = embed_documents(ws_slug, doc_paths)
            print(f"    Embedded: {count} documents")

        # Set system prompt and chat mode
        print("  Configuring workspace settings...")
        update_workspace(ws_slug, {
            "openAiPrompt": config["prompt"],
            "chatMode": config["chat_mode"],
            "similarityThreshold": config["similarity_threshold"]
        })
        print("    System prompt set")
        print(f"    Chat mode: {config['chat_mode']}")
        print()

    # Step 5: Verify with test queries
    print("=" * 60)
    print("[Verification] Testing each workspace with a sample query...")
    print("=" * 60)
    print()

    all_passed = True
    for ws_slug, question in TEST_QUESTIONS.items():
        print(f"  [{ws_slug}]")
        print(f"  Q: {question}")
        try:
            response, sources = test_query(ws_slug, question)
            if sources > 0 and "no relevant information" not in response.lower():
                print(f"  A: {response[:200]}...")
                print(f"  Sources: {sources} document(s) referenced")
                print(f"  Status: PASS")
            else:
                print(f"  A: {response[:200]}")
                print(f"  Status: NEEDS REVIEW (no sources matched)")
                all_passed = False
        except Exception as e:
            print(f"  Status: ERROR - {e}")
            all_passed = False
        print()

    # Summary
    print("=" * 60)
    if all_passed:
        print("Setup complete. All workspaces verified.")
    else:
        print("Setup complete with warnings. Some workspaces may need manual review.")
        print("Try adjusting similarityThreshold (lower = retrieves more) in AnythingLLM.")
    print("=" * 60)


if __name__ == "__main__":
    main()
