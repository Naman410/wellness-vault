# Directive: Generate Sample Data for The Wellness Vault

## Goal
Generate all 15+ realistic but fictional sample data files for the NovaBotanics demo.
These files populate the four AnythingLLM workspaces to demonstrate the Wellness Vault.

## Fictional Brand
**NovaBotanics** - D2C supplement company selling:
- Sleep Gummies (melatonin + L-theanine, recently reformulated)
- Turmeric Blend (with black pepper extract for bioavailability)
- Daily Greens Powder
- Magnesium Supplement

## Inputs
- None (all data is generated, no external API calls needed)
- `.env` → `SAMPLE_DATA_DIR` sets the output path (default: `.tmp/sample_data`)

## Output Files

### Workspace 1: Customer Voice
| File | Format | Rows |
|------|--------|------|
| `amazon_reviews_sleep_gummies.csv` | CSV | 50 rows |
| `shopify_reviews_turmeric_blend.csv` | CSV | 35 rows |
| `support_tickets_q4_2025.csv` | CSV | 28 rows |
| `social_mentions_compiled.txt` | TXT | 25 entries |

### Workspace 2: Team Brain
| File | Format |
|------|--------|
| `NovaBotanics_Brand_Guidelines.txt` | TXT |
| `SOP_New_Product_Launch.txt` | TXT |
| `Meeting_Notes_Q4_Product_Planning.txt` | TXT |
| `Employee_Onboarding_Product_Knowledge.txt` | TXT |
| `Pricing_Strategy_2026.txt` | TXT |

### Workspace 3: Competitor Intel
| File | Format |
|------|--------|
| `Competitor_Analysis_Sleep_Category.txt` | TXT |
| `Market_Trends_Wellness_2026.txt` | TXT |
| `Amazon_Competitor_Listings_Scraped.txt` | TXT |
| `Competitor_Social_Content_Audit.txt` | TXT |

### Workspace 4: Supplier Intel
| File | Format |
|------|--------|
| `COA_KSM66_Ashwagandha_SupplierA.txt` | TXT |
| `Supplier_Pricing_Comparison_2026.csv` | CSV |
| `Supplier_Correspondence_Archive.txt` | TXT |

## Execution
```
python execution/generate_sample_data.py
```

Files are written to `SAMPLE_DATA_DIR` (default `.tmp/sample_data/`), organized into
subdirectories: `customer_voice/`, `team_brain/`, `competitor_intel/`, `supplier_intel/`.

## Patterns to Inject (Critical for Demo)
These specific patterns must appear in the data so the AI surfaces them cleanly:

**Customer Voice:**
- 8 reviews mention gummies melting in summer shipping
- "berry flavor" mentioned in 6 reviews as requested flavor
- "L-theanine" mentioned positively in 5 reviews (post-reformulation)
- Turmeric capsule size complaint in 7 reviews
- 3 reviews explicitly compare to competitor "ZenLeaf" brand

**Team Brain:**
- Reformulation rationale: melatonin reduced 5mg→3mg, L-theanine added 100mg
- Brand voice keywords: "science-backed", "clean label", "no fillers"
- Launch checklist has 12-week timeline with week-by-week milestones

**Supplier Intel:**
- Supplier A (PurePlant) has better price but longer lead time (45 days)
- Supplier B (GreenSource) has faster lead time (21 days) but 15% higher price
- Ashwagandha COA shows heavy metals well within limits

## Notes / Learnings
- Use TXT instead of PDF to avoid PDF generation dependencies (AnythingLLM reads TXT fine)
- Keep individual files focused and under 500 lines — improves RAG retrieval accuracy
- After generating, verify files are readable before ingesting into AnythingLLM
