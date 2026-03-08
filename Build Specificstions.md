\*\*THE WELLNESS VAULT\*\*



Private Product Intelligence Hub



Complete Build Specification - Week 02



For: Digital Wellness D2C Automation Program



Constraint: Private / Offline LLMs Only



Date: March 2026



\# 1\\. Executive Summary



The Wellness Vault is a private, offline AI intelligence hub built for D2C wellness brands. It runs entirely on the client's laptop using Ollama and AnythingLLM - no data ever touches external servers. The system ingests a brand's scattered internal documents (customer reviews, supplier docs, SOPs, competitive research) and lets any team member query them in plain English.



\*\*THE ONE-LINE PITCH\*\*



"Your entire brand's knowledge - customer reviews, supplier docs, internal playbooks, competitor intel - searchable by anyone on your team, in plain English, without a single byte leaving your laptop."



\## Why Private / Offline?



This is not privacy theater. D2C wellness brands handle genuinely sensitive business data daily:



\- \*\*Unreleased product formulations\*\* - trade secrets that define competitive advantage

\- \*\*Supplier pricing and terms\*\* - confidential commercial relationships

\- \*\*Customer health-related feedback\*\* - increasingly regulated under new state laws and the proposed HIPRA legislation

\- \*\*Competitive intelligence files\*\* - strategic analysis they'd never want a competitor to access

\- \*\*Pre-launch marketing strategies\*\* - campaign plans that lose value if leaked early



Sending any of this through cloud-based AI (ChatGPT, Claude API, etc.) means it hits external servers. For a \\$349 billion industry where brands live and die by proprietary formulations and speed-to-market, that's a real risk - not a theoretical one.



\## Safety Posture: Why This Won't Hurt Anyone



\*\*RISK CALIBRATION\*\*



Every use case in this system is "insight generation" - not "decision execution."



If the AI gets something wrong, the worst outcome is: someone spends 30 extra seconds verifying against the source document.



No compliance decisions. No health claims. No regulatory filings. No customer-facing output without human review.



This is a research accelerator, not an autopilot.



\# 2\\. Technical Setup



\## Architecture Overview



The system has three layers, all running locally:



| \*\*Layer\*\* | \*\*Tool\*\* | \*\*Role\*\* |

| --- | --- | --- |

| AI Brain | Ollama | Runs the LLM locally, exposes API at localhost:11434 |

| Chat Interface | AnythingLLM Desktop | Provides workspaces, document ingestion (RAG), prompt templates |

| Data Store | Local filesystem | All documents stay on the laptop, organized by workspace |



\## Step-by-Step Installation



\### Step 1: Install Ollama



Download from: <https://ollama.com/download>



For Mac: Requires macOS Sonoma 14+ for best performance. For Linux, run:



curl -fsSL <https://ollama.com/install.sh> | sh



\### Step 2: Pull the Right Model



\*\*MODEL SELECTION - THIS MATTERS\*\*



Do NOT default to llama3 (8B). It's too weak for nuanced document Q\&A.



Your primary model should be: mistral (7B) for machines with 8GB RAM, or llama3:70b for machines with 32GB+ RAM.



For the demo, use: mistral - it's the best quality-to-speed ratio at 7B parameters and handles RAG tasks well.



Pull it with: ollama pull mistral



Here's the full model decision matrix based on your hardware:



| \*\*RAM\*\* | \*\*Recommended Model\*\* | \*\*Command\*\* | \*\*Best For\*\* |

| --- | --- | --- | --- |

| 8 GB | mistral (7B) | ollama pull mistral | General Q\&A, summaries, first drafts |

| 16 GB | mistral + nomic-embed-text | Pull both models | Better RAG with dedicated embeddings |

| 32 GB+ | llama3:70b or mixtral:8x7b | ollama pull mixtral:8x7b | Complex multi-doc reasoning |

| Weak laptop | Use Google Colab + ngrok tunnel | See Zero-Cost Hack section | Free GPU, not fully offline |



\### Step 3: Verify Ollama is Running



Open terminal and run:



ollama run mistral



Ask it a simple question. If it responds, your AI brain is live. Press Ctrl+D to exit the chat. Verify the API is accessible:



curl <http://localhost:11434/api/tags>



This should return a JSON list of your installed models.



\### Step 4: Install AnythingLLM Desktop



Download from: <https://anythingllm.com>



Install like any desktop app. On first launch:



\- Choose LLM Provider → Select "Ollama"

\- Set Base URL: <http://localhost:11434>

\- Select your model (mistral) from the dropdown

\- For the embedding model: select "nomic-embed-text" if you pulled it, otherwise AnythingLLM's built-in embedder works fine

\- For the vector database: use the default (LanceDB) - it's local and requires no setup



\### Step 5: Create the Four Workspaces



In AnythingLLM, create these four workspaces (one for each priority use case):



| \*\*Workspace Name\*\* | \*\*Purpose\*\* | \*\*Icon Suggestion\*\* |

| --- | --- | --- |

| Customer Voice | Review mining, feedback analysis, sentiment tracking | Chat bubble or megaphone |

| Team Brain | SOPs, brand guidelines, meeting notes, internal knowledge | Brain or lightbulb |

| Competitor Intel | Competitor products, pricing, positioning, market trends | Target or binoculars |

| Supplier Intel | COAs, spec sheets, pricing, supplier comparisons | Document or package |



\# 3\\. Sample Data to Build the Demo



Since this is a portfolio piece, you need realistic but fictional sample data. Here's exactly what to create for each workspace. The fictional brand is "NovaBotanics" - a D2C supplement company selling sleep gummies, a turmeric blend, a daily greens powder, and a magnesium supplement.



\## Workspace 1: Customer Voice (Priority #1)



\*\*Create 3-4 CSV or text files\*\* simulating real review data. Here's the structure:



\*\*File 1: amazon\_reviews\_sleep\_gummies.csv\*\*



Columns: date, rating (1-5), title, review\_text, verified\_purchase



Create 40-50 rows mixing positive, negative, and neutral reviews. Include realistic patterns like:



\- Complaints about taste (too sweet, artificial aftertaste)

\- Praise for effectiveness ("actually fell asleep faster")

\- Shipping complaints (melted gummies in summer)

\- Requests for new flavors ("wish they had a berry option")

\- Comparisons to competitors ("better than Brand X but more expensive")

\- Texture issues ("too sticky", "hard to chew")



\*\*File 2: shopify\_reviews\_turmeric\_blend.csv\*\*



Same structure, 30-40 rows. Patterns to include:



\- Questions about bioavailability ("does this have black pepper extract?")

\- Positive results mentions ("joint comfort improved after 3 weeks")

\- Capsule size complaints ("too large to swallow easily")

\- Pricing sensitivity ("great product but a bit pricey for monthly use")



\*\*File 3: support\_tickets\_q4\_2025.csv\*\*



Columns: date, ticket\_id, product, category, customer\_message, resolution



Create 25-30 rows. Categories: shipping\_issue, product\_quality, subscription\_management, refund\_request, product\_question



\*\*File 4: social\_mentions\_compiled.txt\*\*



A plain text file with 20-30 simulated social media comments (formatted as "@username: comment") from Instagram, TikTok, and Reddit threads about the brand.



\*\*PRO TIP: MAKING SAMPLE DATA REALISTIC\*\*



Use ChatGPT or Claude to generate the sample CSVs. Prompt: "Generate 50 realistic Amazon product reviews for a D2C sleep gummy supplement. Mix of 1-5 star ratings. Include realistic complaints about taste, texture, effectiveness, shipping, and price. CSV format with columns: date, rating, title, review\_text, verified\_purchase."



Then manually inject 5-6 very specific patterns you want the demo to surface (e.g., 8 reviews mentioning melting during shipping) so you can show the AI finding them.



\## Workspace 2: Team Brain (Priority #2)



\*\*Create 4-5 document files\*\* simulating real internal docs:



\- \*\*NovaBotanics\_Brand\_Guidelines.pdf\*\* - 2-3 pages covering brand voice (warm, science-backed, approachable), visual identity, do's and don'ts for social media language

\- \*\*SOP\_New\_Product\_Launch.pdf\*\* - A step-by-step checklist covering timeline (12 weeks), stakeholder sign-offs, testing requirements, marketing prep, channel setup

\- \*\*Meeting\_Notes\_Q4\_Product\_Planning.pdf\*\* - Simulated meeting notes discussing the decision to reformulate the sleep gummies (new melatonin dosage, adding L-theanine), with rationale documented

\- \*\*Employee\_Onboarding\_Product\_Knowledge.pdf\*\* - Overview of the full product line, key ingredients, differentiators vs competitors, FAQs new hires ask

\- \*\*Pricing\_Strategy\_2026.pdf\*\* - Internal pricing rationale, margin targets, subscription discount tiers, wholesale vs D2C pricing



\## Workspace 3: Competitor Intel (Priority #3)



\*\*Create 3-4 files\*\* simulating competitive research:



\- \*\*Competitor\_Analysis\_Sleep\_Category.pdf\*\* - A comparison table of 5-6 competing sleep supplements (fictional names) covering: active ingredients, dosages, price per serving, star rating, key differentiators, packaging format

\- \*\*Market\_Trends\_Wellness\_2026.pdf\*\* - A summary of industry trends: growing demand for stress and mindfulness products, personalization, subscription models, clean label trends, functional mushroom growth

\- \*\*Amazon\_Competitor\_Listings\_Scraped.txt\*\* - Text dumps of 3-4 competitor Amazon product pages (title, bullet points, description, price, rating)

\- \*\*Competitor\_Social\_Content\_Audit.pdf\*\* - Notes on what types of content competitors post, posting frequency, engagement levels, themes that perform well



\## Workspace 4: Supplier Intel (Priority #4)



\*\*Create 3 files\*\* simulating supplier documentation:



\- \*\*COA\_KSM66\_Ashwagandha\_SupplierA.pdf\*\* - A simulated Certificate of Analysis with identity test results, potency, heavy metals, microbial testing

\- \*\*Supplier\_Pricing\_Comparison\_2026.csv\*\* - Columns: supplier, ingredient, price\_per\_kg, MOQ, lead\_time\_days, origin\_country, certifications

\- \*\*Supplier\_Correspondence\_Archive.txt\*\* - A compiled thread of simulated email exchanges with 2-3 suppliers discussing pricing negotiations, delivery issues, and quality concerns



\# 4\\. Prompt Templates for Each Workspace



Set these as the system prompts within each AnythingLLM workspace. They guide the AI's behavior and output format.



\## Workspace 1: Customer Voice - System Prompt



\*\*SYSTEM PROMPT\*\*



You are a Customer Insights Analyst for a D2C wellness supplement brand. Your job is to analyze customer reviews, support tickets, and social media feedback to surface actionable insights.



When answering questions about customer feedback, always:



1\\. Cite specific reviews or tickets when possible (quote the relevant text).



2\\. Quantify patterns when you can (e.g., "7 out of 50 reviews mention this").



3\\. Separate facts from interpretations - state what the data says, then offer your analysis.



4\\. Flag when sample sizes are too small to draw reliable conclusions.



5\\. Suggest follow-up questions the team should investigate.



Output format: Start with a brief summary (2-3 sentences), then provide supporting details with specific examples. End with recommended next steps.



Important: You are an internal research tool. Your outputs will always be reviewed by a human before any decisions are made. If you're unsure about something, say so clearly.



\*\*Demo Questions to Ask (in this order for video):\*\*



\- "What are the top 5 complaints about our sleep gummies?"

\- "Are customers asking for any specific new flavors? Which ones come up most?"

\- "Compare the sentiment between our sleep gummies and our turmeric blend - which product has more positive reviews?"

\- "What are the most common reasons customers contact support? Any patterns by product?"

\- "Pull out any reviews that mention competitor products - what do customers say we do better or worse?"

\- "Based on all the feedback, what's the single biggest product improvement we should prioritize this quarter?"



\## Workspace 2: Team Brain - System Prompt



\*\*SYSTEM PROMPT\*\*



You are the internal knowledge assistant for NovaBotanics. You have access to the company's SOPs, brand guidelines, meeting notes, and product documentation.



When answering questions:



1\\. Always reference which specific document your answer comes from.



2\\. If the answer isn't in the documents, say "I don't have this information in my current documents" - never make something up.



3\\. For process questions, provide step-by-step answers when the SOP supports it.



4\\. For historical questions ("why did we decide X?"), reference the relevant meeting notes or decision documents.



5\\. Keep answers concise but complete.



You are a search and retrieval tool, not a decision-maker. Always defer to the actual documents and the humans who wrote them.



\*\*Demo Questions:\*\*



\- "What's our brand voice? Give me the key do's and don'ts for social media."

\- "Walk me through the new product launch process step by step."

\- "Why did we decide to reformulate the sleep gummies? What changed?"

\- "I'm new here - give me a quick overview of our full product line and what makes each product different."

\- "What's our pricing strategy for subscriptions vs one-time purchases?"



\## Workspace 3: Competitor Intel - System Prompt



\*\*SYSTEM PROMPT\*\*



You are a Competitive Intelligence Analyst for a D2C wellness supplement brand. You analyze competitor products, pricing, positioning, and market trends.



When answering:



1\\. Be specific - reference actual competitor names, ingredients, prices from the documents.



2\\. Always compare back to our products when relevant.



3\\. Identify gaps and opportunities, not just descriptions.



4\\. Flag when data might be outdated (check document dates).



5\\. Present findings in a structured format: Findings → Implications → Recommended Actions.



This is strategic analysis for internal use only. Your outputs inform decisions but do not make them.



\*\*Demo Questions:\*\*



\- "How does our sleep gummy compare to the top 3 competitors on ingredients and price?"

\- "What ingredients are trending in the wellness space that we're not using yet?"

\- "What type of social content is working best for our competitors?"

\- "Where is our biggest competitive gap - product, pricing, or marketing?"



\## Workspace 4: Supplier Intel - System Prompt



\*\*SYSTEM PROMPT\*\*



You are a Supply Chain Analyst for a D2C wellness supplement brand. You analyze supplier documentation including Certificates of Analysis (COAs), pricing sheets, and correspondence.



When answering:



1\\. Reference specific suppliers, prices, and test results from the documents.



2\\. For comparison questions, present data in a clear format showing each supplier side by side.



3\\. Flag any quality concerns (e.g., heavy metal levels close to limits, missing certifications).



4\\. Note lead times and MOQ constraints that affect procurement decisions.



5\\. Always specify the date of the data you're referencing.



This tool assists procurement research. All purchasing decisions require human approval and direct supplier verification.



\# 5\\. Sunday Demo Video Script



Target length: 3-5 minutes. Here's the exact script structure:



\## Scene 1: The Hook (0:00 - 0:30)



\*\*SCRIPT\*\*



\\\[Screen: Dark slide with text\\]



"The average D2C wellness brand has their proprietary formulations, customer health data, and competitive strategy scattered across 47 different files, emails, and spreadsheets."



\\\[Beat\\]



"And right now, to make sense of any of it, they either dig through folders for 20 minutes... or paste it into ChatGPT, where it sits on someone else's servers."



\\\[Beat\\]



"We built something different."



\## Scene 2: The Architecture (0:30 - 1:00)



\*\*SCRIPT\*\*



\\\[Screen: Show simple architecture diagram\\]



"This is the Wellness Vault. It runs 100% on this laptop. Ollama handles the AI brain. AnythingLLM provides the interface. And every document stays right here - private, offline, air-gapped."



\\\[Quick: Show terminal with ollama running, show AnythingLLM connected\\]



"Let me show you what it can actually do."



\## Scene 3: Customer Voice Demo (1:00 - 2:30)



\*\*SCRIPT\*\*



\\\[Screen: AnythingLLM - Customer Voice workspace\\]



"This workspace has ingested 3 months of Amazon reviews, Shopify reviews, and support tickets for a wellness supplement brand. Watch what happens when I ask it a simple question."



\\\[Type: "What are the top 5 complaints about our sleep gummies?"\\]



\\\[Wait for response - show the AI surfacing specific patterns with quoted reviews\\]



"In 15 seconds, it found what would take a team member 2 hours of spreadsheet digging. And look - it's citing specific reviews, giving me counts, and even suggesting follow-up questions."



\\\[Type: "Are customers asking for new flavors? Which ones?"\\]



\\\[Show response\\]



"That's a product development insight that was buried in 200 reviews. Now it's on my screen in seconds."



\## Scene 4: Team Brain Demo (2:30 - 3:30)



\*\*SCRIPT\*\*



\\\[Switch to Team Brain workspace\\]



"Now imagine it's a new hire's first week. Instead of bugging five different people, they ask the Vault."



\\\[Type: "I'm new here. Walk me through our full product line and what makes each product different."\\]



\\\[Show response pulling from onboarding docs\\]



\\\[Type: "Why did we reformulate the sleep gummies last quarter?"\\]



\\\[Show response referencing meeting notes with specific rationale\\]



"Every decision, every SOP, every brand guideline - instantly searchable. No more 'Hey does anyone remember why we changed the formula?' in Slack."



\## Scene 5: The Close (3:30 - 4:00)



\*\*SCRIPT\*\*



\\\[Screen: Architecture diagram again\\]



"Four workspaces. Zero cloud dependencies. Every query answered from your own data, on your own machine."



"This is Week 2 of a 14-week automation suite built specifically for digital wellness brands. Each week adds another layer. And the Wellness Vault becomes the intelligence foundation that powers everything else."



\\\[End card with contact info\\]



\# 6\\. Monetization Strategy



\## Pricing Tiers



| \*\*Tier\*\* | \*\*Price\*\* | \*\*Includes\*\* | \*\*Target Client\*\* |

| --- | --- | --- | --- |

| Starter Setup | \\$1,500 - 2,500 one-time | Ollama + AnythingLLM install, 2 workspaces configured, initial document ingestion, 1 hour team training | Small brands (2-10 people), testing the concept |

| Full Vault | \\$3,000 - 5,000 one-time | All 4 workspaces, full document ingestion, custom prompt templates, brand-specific tuning, 2 hours team training | Mid-size brands (10-50 people), serious about the tool |

| Managed Vault | \\$500 - 1,500/month | Full setup + monthly document refresh, prompt optimization, insight reports, priority support | Brands wanting ongoing intelligence, not just a tool |

| Vault + Suite Bundle | \\$8,000 - 15,000 | The Wellness Vault + select automations from weeks 3-14, packaged as a complete operations upgrade | Best value play once you've built the full 14-week suite |



\## Revenue Justification



The value proposition is simple time savings math:



\- A product manager spends 5-8 hours/week digging through reviews, docs, and spreadsheets for answers

\- At a fully-loaded cost of \\$50-75/hour, that's \\$1,000-2,400/month in lost productivity

\- The Wellness Vault reduces that to minutes per query

\- A \\$1,500 one-time setup pays for itself within 4-6 weeks



For the managed tier, the monthly cost is less than a single hour of a regulatory consultant's time, while providing unlimited queries.



\# 7\\. Build Checklist - Day by Day



| \*\*Day\*\* | \*\*Task\*\* | \*\*Time Est.\*\* | \*\*Deliverable\*\* |

| --- | --- | --- | --- |

| Day 1 | Install Ollama, pull mistral model, verify API works | 1-2 hours | Working local LLM |

| Day 1 | Install AnythingLLM, connect to Ollama, test basic chat | 1 hour | Connected interface |

| Day 2 | Generate all sample data files (use ChatGPT/Claude to help) | 2-3 hours | 15+ realistic data files |

| Day 2 | Create the 4 workspaces in AnythingLLM | 30 min | 4 empty workspaces |

| Day 3 | Ingest documents into each workspace, set system prompts | 2 hours | 4 populated workspaces |

| Day 3 | Test all demo questions, refine prompts based on output quality | 2-3 hours | Tested prompt templates |

| Day 4 | Run through full demo flow 2-3 times, note any weak spots | 1-2 hours | Polished demo flow |

| Day 4 | Create architecture diagram (use Excalidraw or Canva) | 30 min | Visual for demo video |

| Day 5 | Record demo video following the script in Section 5 | 2-3 hours | Final video file |

| Day 5 | Write LinkedIn post / portfolio description | 1 hour | Published portfolio piece |



\*\*TOTAL BUILD TIME: 15-20 HOURS ACROSS 5 DAYS\*\*



This is intentionally front-loaded on Days 1-3 so you have Days 4-5 for polishing.



If you finish early, use extra time to add the 5th workspace (Content First-Draft Engine) as a bonus.



\# 8\\. Gaps, Limitations \& Honest Callouts



These are things you need to be aware of and disclose to potential clients. Hiding them will damage your credibility far more than acknowledging them.



\## Limitation 1: Local Model Quality vs Cloud



Mistral 7B is good, but it's not GPT-4 or Claude Opus. For simple lookups and pattern recognition ("find all reviews mentioning taste"), it's excellent. For nuanced multi-document reasoning ("synthesize insights across 5 different data sources and draw a strategic conclusion"), it will sometimes miss things or produce shallow analysis.



\*\*Mitigation:\*\* Position the tool as "your first researcher, not your final analyst." It does 80% of the digging work; humans do the 20% of critical thinking.



\## Limitation 2: RAG Accuracy



AnythingLLM's RAG (Retrieval Augmented Generation) sometimes retrieves the wrong chunks of text when documents are long or similar. This means the AI might answer based on the wrong section of a document.



\*\*Mitigation:\*\* Keep documents focused and well-named. A 2-page COA is better than a 50-page combined supplier binder. Break large files into smaller, topic-specific ones. This dramatically improves retrieval accuracy.



\## Limitation 3: No Real-Time Updates



The system only knows about documents that have been manually uploaded. It won't automatically pull new Amazon reviews or sync with Shopify. Someone needs to periodically export and upload fresh data.



\*\*Mitigation:\*\* This is actually the basis for the managed service tier - you do the data refresh for them monthly. Also, later weeks in your 14-week program (e.g., if you build a scraping or API integration automation) can feed into the Vault automatically.



\## Limitation 4: Hardware Dependency



If the client's laptop has only 8GB RAM, the experience will be slow. Response times of 30-60 seconds for complex queries are common on lower-end machines. Clients with M1/M2/M3 Macs or 16GB+ RAM will have a much better experience.



\*\*Mitigation:\*\* Always check hardware specs before scoping the project. For weak laptops, offer the Google Colab + ngrok hack as a compromise (not fully offline but free and fast). Be upfront about response time expectations.



\## Limitation 5: No Multi-User Access



AnythingLLM Desktop runs on one machine. If a team of 10 people needs access, they can't all use it simultaneously. The Docker deployment option (AnythingLLM server mode) solves this but requires more setup.



\*\*Mitigation:\*\* For the demo and small teams, single-machine is fine. For larger deployments, scope Docker setup as an add-on service. This is also a natural upsell.



\# 9\\. How This Connects to Weeks 3-14



The Wellness Vault is not just a standalone product - it becomes the data foundation that makes every subsequent automation more valuable. Here's how:



| \*\*Future Week Topic (Likely)\*\* | \*\*How It Connects to the Vault\*\* |

| --- | --- |

| Email Marketing Automation | Pull customer voice insights to personalize email campaigns by segment |

| Social Media Scheduling | Use competitor content audit data to inform content strategy |

| Customer Service Chatbot | Team Brain workspace becomes the chatbot's knowledge base |

| Reporting Dashboard | All four workspaces feed data into a unified insights dashboard |

| CRM / Lead Management | Customer voice data enriches lead profiles with sentiment and preferences |

| Product Development Pipeline | Review mining directly feeds the product roadmap |

| Supplier Management | Supplier Intel workspace automates vendor comparison workflows |

| Content Generation | Brand guidelines + customer language inform content creation at scale |



\*\*This is the key selling point when bundling:\*\* the Vault is like the hard drive of the entire automation suite. Each additional automation reads from and writes to it, creating a compounding intelligence loop that gets smarter with every week you add.



\# 10\\. Portfolio Positioning for Inbound Leads



\## LinkedIn / Portfolio Description



\*\*PORTFOLIO COPY\*\*



The Wellness Vault | Private AI Intelligence Hub for D2C Brands



Problem: D2C wellness brands sit on goldmines of internal data - customer reviews, supplier docs, competitive research, team knowledge - but it's scattered across dozens of tools, and too sensitive to run through cloud AI.



Solution: A fully offline, private AI system that ingests all internal documents and lets anyone on the team query them in plain English. Runs on the client's own hardware. Zero data leaves the machine.



Built with: Ollama (local LLM), AnythingLLM (RAG interface), Mistral 7B



Impact: Turns 2-hour research tasks into 15-second queries. Onboards new hires in minutes instead of weeks. Surfaces customer insights that were previously invisible.



Part of a 14-automation suite built specifically for digital wellness brands.



\## Ideal Inbound Lead Profile



When sharing this portfolio piece, target these specific roles:



\- \*\*Founders / CEOs of D2C supplement brands\*\* with 5-50 employees who are scaling and drowning in data

\- \*\*Operations managers at wellness brands\*\* who are currently the "human search engine" for their team

\- \*\*Product managers at supplement companies\*\* who spend hours manually analyzing reviews and competitor data

\- \*\*Wellness brand marketing agencies\*\* who manage multiple client accounts and need a knowledge layer per client



\_End of Build Specification\_



\*\*Now go build it.\*\*

