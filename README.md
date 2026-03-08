# The Wellness Vault

**Private AI Intelligence Hub for D2C Wellness Brands**

A fully offline, private AI system that ingests a brand's internal documents (customer reviews, supplier docs, SOPs, competitive research) and lets any team member query them in plain English. Built with local LLMs — no data ever leaves the machine.

## Why This Exists

D2C wellness brands handle genuinely sensitive data daily:

- Unreleased product formulations (trade secrets)
- Supplier pricing and contract terms (confidential)
- Customer health-related feedback (increasingly regulated)
- Competitive intelligence files (strategic)

Sending any of this through cloud AI means it hits external servers. The Wellness Vault keeps everything local, private, and air-gapped.

## Architecture

```
+-------------------+     +-------------------+     +-------------------+
|   Data Sources    | --> |   Python Scripts   | --> |   AnythingLLM     |
|  (reviews, docs,  |     |   (execution/)     |     |   (RAG + Chat)    |
|   supplier data)  |     |                    |     |                    |
+-------------------+     +-------------------+     +-------------------+
                                    |                        |
                                    v                        v
                          +-------------------+     +-------------------+
                          |   Ollama (Local)   |     |   LanceDB         |
                          |   LLM + Embeddings |     |   (Vector Store)   |
                          +-------------------+     +-------------------+
```

**Everything runs on the client's laptop.** Zero cloud dependencies.

| Layer | Tool | Role |
|-------|------|------|
| AI Brain | Ollama | Runs the LLM locally, provides embeddings |
| Chat Interface | AnythingLLM Desktop | Workspaces, document ingestion (RAG), chat UI |
| Vector Storage | LanceDB (built-in) | Stores document embeddings for semantic search |
| Automation | Python scripts | Data generation, workspace setup via API |

## Project Structure

```
execution/              Python scripts (deterministic tools)
  generate_sample_data.py   Generate 16 demo files for NovaBotanics
  setup_workspaces.py       Configure AnythingLLM workspaces via API

directives/             SOPs in Markdown (living instruction docs)
  generate_sample_data.md   SOP for sample data generation
  setup_workspaces.md       SOP for workspace setup automation

.tmp/                   All intermediates (gitignored, always regenerated)
  sample_data/
    customer_voice/     Amazon reviews, Shopify reviews, support tickets, social mentions
    team_brain/         Brand guidelines, SOPs, meeting notes, pricing strategy
    competitor_intel/   Competitor analysis, market trends, competitor listings
    supplier_intel/     COAs, supplier pricing, supplier correspondence

.env                    Environment variables (gitignored)
CLAUDE.md               AI orchestration instructions (3-layer architecture)
```

## The Demo Brand: NovaBotanics

A fictional D2C supplement company selling sleep gummies, turmeric blend, daily greens powder, and magnesium supplements. All sample data is generated with realistic patterns that the AI can surface:

- 8 reviews mention melted gummies (summer shipping issue)
- 6 reviews request berry flavor
- 5 reviews praise the L-theanine reformulation
- 3 reviews compare to competitor "ZenLeaf"
- Meeting notes document the reformulation decision (melatonin 5mg to 3mg, L-theanine 100mg added)
- Supplier comparison: PurePlant ($272/kg, 45-day lead) vs GreenSource (faster but 15% pricier)

## Setup Instructions

### Prerequisites

- Python 3.8+
- [Ollama](https://ollama.com/download) installed
- [AnythingLLM Desktop](https://anythingllm.com) installed

### Step 1: Clone and configure

```bash
git clone <repo-url>
cd wellness-vault
```

Create a `.env` file:

```
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama3.2:3b
ANYTHINGLLM_BASE_URL=http://localhost:3001
ANYTHINGLLM_API_KEY=your_api_key_here
SAMPLE_DATA_DIR=.tmp/sample_data
```

### Step 2: Pull Ollama models

```bash
ollama pull llama3.2:3b        # Main LLM — fits in 4GB VRAM (~2GB)
ollama pull nomic-embed-text   # Embedding model (~270MB)
```

### Step 3: Configure AnythingLLM

1. Open AnythingLLM Desktop
2. Settings > LLM Provider > **Ollama** > `http://localhost:11434`
3. Settings > Embedding > **Ollama** > `nomic-embed-text`
4. Settings > Developer API > **Enable** > copy the API key to `.env`
5. Create 4 workspaces: Customer Voice, Team Brain, Competitor Intel, Supplier Intel

### Step 4: Install Python dependencies

```bash
pip install requests python-dotenv
```

### Step 5: Generate sample data

```bash
python execution/generate_sample_data.py
```

Generates 16 realistic data files across 4 workspace directories.

### Step 6: Setup workspaces via API

Make sure Ollama and AnythingLLM are both running, then:

```bash
python execution/setup_workspaces.py
```

This uploads all documents, embeds them into the correct workspaces, sets custom system prompts, and enables RAG mode.

### Step 7: Test it

Open AnythingLLM and ask:

- **Customer Voice**: "What are the top 5 complaints about our sleep gummies?"
- **Team Brain**: "Why did we reformulate the sleep gummies?"
- **Competitor Intel**: "How does our sleep gummy compare to the top 3 competitors?"
- **Supplier Intel**: "Compare our suppliers on price and lead time for KSM-66"

## How It Works

### The 3-Layer Architecture

This project follows a 3-layer architecture that separates concerns:

1. **Directives** (`directives/`): SOPs in Markdown. Define goals, inputs, tools, outputs, and edge cases.
2. **Orchestration** (Claude/AI): Reads directives, calls execution tools, handles errors, updates directives with learnings.
3. **Execution** (`execution/`): Deterministic Python scripts. API calls, data processing, file operations. Reliable and testable.

**Why**: If you do everything in the LLM, errors compound. 90% accuracy per step = 59% success over 5 steps. Push complexity into deterministic code.

### The RAG Pipeline

```
Sample Data Files --> AnythingLLM API Upload --> Ollama Embeddings --> LanceDB Vector Store
                                                                            |
User Question --> AnythingLLM Chat --> Semantic Search --> Relevant Chunks --> LLM Response
```

1. Documents are uploaded to AnythingLLM via its REST API
2. AnythingLLM chunks the documents and sends each chunk to Ollama's `nomic-embed-text` for embedding
3. Embeddings are stored in LanceDB (local vector database)
4. When a user asks a question, AnythingLLM searches for semantically similar chunks
5. The matching chunks are sent to the LLM as context alongside the question
6. The LLM generates an answer grounded in the actual documents

### For Real Clients (Future Automation)

The current setup uses generated sample data. For real clients, the architecture extends:

```
Shopify API  --+
Zendesk API  --+--> Fetch Scripts --> .tmp/ --> AnythingLLM API --> LanceDB
Amazon API   --+    (scheduled)      (files)   (auto-upload)      (vector store)
```

The fetch scripts replace the sample data generator. Everything downstream (upload, embed, query) stays identical.

## Hardware Requirements

| RAM | Recommended Model | Response Time |
|-----|------------------|---------------|
| 8GB RAM, no GPU | llama3.2:3b (CPU) | ~15-30s |
| 16GB RAM, no GPU | llama3.2:3b (CPU) | ~8-15s |
| NVIDIA GPU (4GB VRAM) | llama3.2:3b (GPU) ✓ this build | ~3-6s |
| NVIDIA GPU (6GB+ VRAM) | mistral 7B or similar | ~3-8s |
| 32GB+ RAM | llama3:70b or mixtral:8x7b | ~5-10s |

## Known Limitations

1. **Local model quality**: llama3.2:3b is excellent for pattern recognition and document search, but won't match GPT-4/Claude for nuanced multi-document reasoning. Position as "first researcher, not final analyst."
2. **RAG accuracy**: Keep documents focused and well-named. Small, topic-specific files retrieve better than large combined docs.
3. **No real-time updates**: Data must be manually exported and re-ingested (or automated via fetch scripts for real clients).
4. **Single-user**: AnythingLLM Desktop runs on one machine. Docker deployment needed for multi-user access.
5. **CSV embedding**: AnythingLLM's API doesn't embed CSV files reliably. The setup script converts CSVs to readable TXT format automatically.

## Part of a Larger System

The Wellness Vault is Week 2 of a 14-week D2C automation suite. It becomes the intelligence foundation that powers subsequent automations — email marketing, social scheduling, customer service, reporting dashboards, and more. Each week adds a layer. The Vault is the data backbone.
