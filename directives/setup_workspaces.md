# Directive: Setup AnythingLLM Workspaces

## Goal
Programmatically configure all 4 AnythingLLM workspaces via API:
upload documents, embed them into the vector database, set system prompts,
and enable RAG (query) mode.

## Inputs
- `.env` → `ANYTHINGLLM_API_KEY`, `ANYTHINGLLM_BASE_URL`
- `.tmp/sample_data/{workspace}/` → generated sample data files
- Ollama must be running (provides embedding model)
- AnythingLLM must be running (provides API + vector DB)

## Script
```
python execution/setup_workspaces.py
```

## What It Does

### Step 1: CSV to TXT Conversion
AnythingLLM's embedder handles plain text better than raw CSV.
The script converts all CSV files to readable TXT format before upload.

### Step 2: Upload Documents
Uses `POST /api/v1/document/upload` to stage each file.
Returns a document path used for embedding.

### Step 3: Embed Documents
Uses `POST /api/v1/workspace/{slug}/update-embeddings` to embed
each document into its workspace's vector database (LanceDB).
Documents are embedded one-by-one for reliability.

### Step 4: Configure Workspaces
Uses `POST /api/v1/workspace/{slug}/update` to set:
- System prompt (persona-specific, from Build Spec Section 4)
- Chat mode: `query` (RAG mode — searches documents before answering)
- Similarity threshold: 0.25

### Step 5: Verification
Sends a test query to each workspace and checks for:
- Non-empty response with document sources
- Correct RAG retrieval (not just generic LLM output)

## Workspace → File Mapping

| Workspace | Source Dir | Files |
|-----------|-----------|-------|
| customer-voice | customer_voice/ | 4 TXT files (reviews, tickets, social) |
| team-brain | team_brain/ | 5 TXT files (guidelines, SOPs, notes, pricing) |
| competitor-intel | competitor_intel/ | 4 TXT files (analysis, trends, listings, audit) |
| supplier-intel | supplier_intel/ | 3 TXT files (COA, pricing, correspondence) |

## API Endpoints Used
- `GET /api/v1/auth` — verify API key
- `POST /api/v1/document/upload` — stage a document
- `POST /api/v1/workspace/{slug}/update-embeddings` — embed into workspace
- `POST /api/v1/workspace/{slug}/update` — set workspace config
- `POST /api/v1/workspace/{slug}/chat` — send query (verification)
- `GET /api/v1/workspace/{slug}` — check workspace state

## Notes / Learnings
- CSV files don't embed properly through the API — must convert to TXT first
- Ollama must be running or embedding fails silently (no error, just 0 docs embedded)
- Embedding documents one-by-one is more reliable than batch
- Verification queries can be slow on CPU-only setups (Mistral 7B on CPU ~30-120s)
- The script is idempotent: clears existing docs before re-embedding
- Known issue: if a file is uploaded multiple times (creating duplicates in staging), subsequent
  embeddings of that filename may silently fail. If files fail to embed, upload them manually
  through the AnythingLLM GUI as a fallback.
- Affected files in testing: shopify_reviews_turmeric_blend.txt, Supplier_Correspondence_Archive.txt
  These embedded successfully via the AnythingLLM UI but not the API when duplicates existed.
