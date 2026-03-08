"""
Generate all sample data files for The Wellness Vault demo.
Fictional brand: NovaBotanics

Usage: python execution/generate_sample_data.py
Output: .tmp/sample_data/{workspace}/filename
"""

import os
import csv
import random
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(os.getenv("SAMPLE_DATA_DIR", ".tmp/sample_data"))

WORKSPACES = ["customer_voice", "team_brain", "competitor_intel", "supplier_intel"]

def setup_dirs():
    for ws in WORKSPACES:
        (BASE_DIR / ws).mkdir(parents=True, exist_ok=True)

def write_csv(path, headers, rows):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(headers)
        w.writerows(rows)
    print(f"  Written: {path}")

def write_txt(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  Written: {path}")

# ─────────────────────────────────────────────
# WORKSPACE 1: CUSTOMER VOICE
# ─────────────────────────────────────────────

def gen_amazon_reviews():
    rows = []

    # Injected patterns (8 melting, 6 berry, 5 L-theanine, competitor ZenLeaf x3)
    injected = [
        ("2025-07-15", 2, "Melted into a blob", "Ordered these for my mom and they arrived completely melted. It's summer and the packaging offers zero insulation. The gummies were fused into one giant sticky mass. NovaBotanics needs to add ice packs or warn buyers. Disappointed.", True),
        ("2025-07-22", 1, "Summer shipping disaster", "These melted completely in transit. I've seen other reviews say the same thing. Eight of my gummies were one clump. Product itself smells great but melted gummies are unusable.", True),
        ("2025-08-01", 2, "Arrived melted", "Third time ordering. First two times were fine. This time they were melted solid. Must be a summer shipping issue — the warehouse or carrier is not keeping them cool. Please fix.", True),
        ("2025-08-05", 2, "Melted gummies again", "Same as other reviewers — melted during shipping. I contacted support and they reshipped but the replacements also melted. Fix the packaging please.", True),
        ("2025-08-10", 3, "Melted but effective", "Gummies arrived partially melted and stuck together. Had to pry them apart. But once I started taking them I did notice I fell asleep faster so the product works. Just fix the shipping.", True),
        ("2025-06-30", 2, "Summer heat kills these", "Beautiful product, terrible packaging for summer. Mine melted. Friends who ordered the same week had melted gummies too. This is clearly a systemic problem in hot months.", True),
        ("2025-07-08", 1, "Melted mess", "Opened the bottle and found a single giant gummy blob. Melted completely. This is the 4th review I've seen about melting. NovaBotanics please use temperature-controlled shipping.", True),
        ("2025-07-19", 3, "Melted but they separated", "Arrived melted together but I was able to separate them once cooled. Still annoying. The product itself is great — the new formula with L-theanine is noticeably calming.", True),
        # Berry flavor requests
        ("2025-09-10", 4, "Love these, wish there was a berry option", "These are my favorite sleep gummies. The mango flavor is good but I'd really love a berry option — blueberry or mixed berry would be amazing. Please make it happen NovaBotanics!", True),
        ("2025-10-02", 5, "Great product, berry flavor please!", "Five stars for effectiveness. My only request: add a berry flavor. I've seen other reviewers ask for this too. Strawberry or mixed berry would be perfect.", True),
        ("2025-09-25", 4, "Works great, would buy berry flavor", "Really happy with these. Fell asleep within 30 minutes both nights I tried them. One thing: I wish they came in berry. The mango is fine but berry would be my preference.", False),
        ("2025-11-01", 5, "Incredible sleep, need berry ASAP", "Best sleep I've had in years. Seriously. The L-theanine addition in the new formula makes a huge difference — I feel calm not just sleepy. But please add a berry flavor option!", True),
        ("2025-10-15", 4, "Good but want berry flavor", "Solid product. Works as advertised. My whole family uses them now. We all agree — berry flavor would make us 5-star reviewers. Specifically mixed berry or blueberry.", True),
        ("2025-09-18", 3, "Average taste, prefer berry", "Effective product but the mango flavor isn't for me. If they made a berry version I'd reorder immediately. Right now I'm looking at alternatives just because of flavor.", False),
        # L-theanine praise (post-reformulation)
        ("2025-10-20", 5, "New formula is a game changer", "I've been using NovaBotanics sleep gummies for 8 months. The new formula with L-theanine is SO much better. I wake up refreshed instead of groggy. The old formula knocked me out too hard.", True),
        ("2025-11-05", 5, "L-theanine addition is perfect", "Whoever added L-theanine to the new formula deserves a raise. That calm, focused drowsiness is exactly what I needed. No more foggy mornings. 10/10.", True),
        ("2025-10-28", 5, "Best sleep supplement I've tried", "Tried about 12 different sleep supplements. This new formula with L-theanine + lower melatonin hits different. Actually fall asleep faster and stay asleep. Not groggy.", True),
        ("2025-11-12", 4, "New formula much better", "The updated formula is a real improvement. Lower melatonin means I don't wake up groggy, and the L-theanine keeps me calm without a knockout effect. Good call NovaBotanics.", True),
        ("2025-10-31", 5, "L-theanine makes the difference", "I was skeptical about the reformulation but L-theanine genuinely helps with the quality of sleep, not just speed of falling asleep. Recommend to anyone with racing thoughts at bedtime.", True),
        # ZenLeaf comparisons
        ("2025-09-05", 4, "Better than ZenLeaf but pricier", "Switched from ZenLeaf Sleep Support to these. NovaBotanics wins on ingredient quality and taste. ZenLeaf uses artificial flavors and higher melatonin. NovaBotanics is $5 more per bottle though.", True),
        ("2025-10-10", 5, "Way better than ZenLeaf", "My wife used ZenLeaf for a year. We switched to NovaBotanics and neither of us is going back. The clean ingredients and no-filler label is exactly what we wanted. ZenLeaf has too many additives.", True),
        ("2025-11-08", 3, "ZenLeaf is cheaper FYI", "These are good but ZenLeaf is 30% cheaper and I honestly can't feel a huge difference. If price matters to you, ZenLeaf is worth considering. NovaBotanics wins on label cleanliness though.", False),
        # General positive reviews
        ("2025-08-20", 5, "Actually works!", "I've tried so many sleep gummies. These actually work. Fell asleep faster every night this week. No grogginess in the morning. Clean ingredients.", True),
        ("2025-09-01", 5, "My new nightly routine", "Take 2 gummies 30 min before bed, fall asleep within 20 minutes. Sleep 7-8 hours straight. Wake up refreshed. These are the real deal.", True),
        ("2025-11-20", 5, "Great for anxiety-driven insomnia", "I have trouble falling asleep because my brain won't quiet down. These gummies calm the mental chatter. The combo of low melatonin + L-theanine is perfect for me.", True),
        ("2025-10-05", 4, "Solid sleep supplement", "Good product. Works consistently. Taste is fine — a little sweet for me but tolerable. Will reorder.", True),
        ("2025-09-12", 4, "Works as described", "Helps me fall asleep faster. Not a miracle cure but a solid, consistent improvement. Appreciate the clean label.", False),
        # Negative/complaints
        ("2025-08-25", 2, "Too sweet for me", "The mango flavor is way too sweet. Almost candy-like. I can taste the added sugars. Wish they had a less sweet option or used stevia only.", True),
        ("2025-09-30", 3, "Artificial aftertaste", "There's a slight artificial aftertaste that lingers. Might be the natural flavoring. Doesn't affect the sleep quality but it's noticeable.", True),
        ("2025-10-22", 2, "Too sticky, hard to separate", "These gummies stick together in the bottle, especially in warm weather. I have to pry them apart and they leave residue on my fingers. Quality control issue.", True),
        ("2025-11-15", 3, "Expensive for what you get", "These are good but at $34 for 60 gummies you're paying a premium. Similar products exist for less. Worth it if you want clean ingredients, but budget buyers look elsewhere.", False),
        ("2025-09-08", 2, "Didn't work for me", "Tried for 2 weeks straight. Zero effect on my sleep. Maybe I'm just resistant to melatonin. Returning.", True),
        ("2025-10-18", 3, "Texture is off", "The texture is harder than I expected — almost like gummy bears rather than soft gummies. Not terrible but not the soft, chewy texture I prefer.", True),
        ("2025-11-03", 1, "Subscription cancelled me without notice", "Product is fine but they cancelled my subscription without telling me and I ran out. Customer service eventually fixed it but I lost a week. Fix your subscription management.", True),
        # Mixed/neutral
        ("2025-08-15", 3, "Decent but not amazing", "Does what it says. Falls asleep a bit faster. Nothing revolutionary. Probably won't reorder given the price.", False),
        ("2025-09-22", 4, "Good for occasional use", "I use these 3-4 nights a week when I need help winding down. Work consistently and I don't feel dependent on them.", True),
        ("2025-10-30", 4, "Better than melatonin pills", "Much prefer gummies over pills. The lower melatonin dose in the new formula is better — less groggy in the AM. Good product.", True),
        ("2025-11-18", 5, "Recommended by my doctor", "My sleep doctor recommended these specifically for the lower melatonin + L-theanine combo. She said most sleep gummies have too much melatonin. These are calibrated right.", True),
        ("2025-08-30", 4, "Great for travel", "Use these when traveling across time zones. Helps reset my sleep schedule. Compact bottle fits in my carry-on.", True),
        ("2025-10-12", 3, "Inconsistent effects", "Works great some nights, barely noticeable others. Maybe I just have inconsistent sleep hygiene. The product is fine.", False),
        ("2025-11-10", 5, "My whole household uses these", "Me, my partner, and my college-aged daughter all use these now. Different sleep issues — all improved. We buy 3 bottles at a time.", True),
        ("2025-09-14", 4, "Good value if you subscribe", "Steep at full price but the subscription discount makes it competitive. 20% off auto-ship is a good deal.", True),
        ("2025-10-25", 2, "Packaging is not resealable", "The bottle cap is fine but the inner seal tears badly and there's no resealable inner bag. Minor complaint but the gummies could dry out.", True),
        ("2025-11-22", 5, "Best sleep in years", "I'm 58 and have had sleep issues for a decade. These are the first supplement that actually helps without side effects. The science-backed formula is the real deal.", True),
        ("2025-09-28", 3, "Average taste, great sleep", "Taste is just OK but the sleep quality improvement is real. Trade-off I'm willing to make.", True),
        ("2025-10-08", 4, "Would recommend", "Simple, effective, clean label. What more do you need? Good sleep supplement.", True),
        ("2025-11-14", 3, "Need bigger bottle option", "60 gummies at 2/night is only 30 days. Wish they sold a 120-count bottle. Would save on shipping and be more economical.", True),
    ]

    for date, rating, title, text, verified in injected:
        rows.append([date, rating, title, text, "Yes" if verified else "No"])

    write_csv(
        BASE_DIR / "customer_voice" / "amazon_reviews_sleep_gummies.csv",
        ["date", "rating", "title", "review_text", "verified_purchase"],
        rows
    )


def gen_shopify_reviews():
    rows = [
        ("2025-08-10", 5, "turmeric_blend", "Finally a turmeric supplement with black pepper extract! The bioavailability difference is real. My joints feel noticeably better after 3 weeks. Will keep ordering.", "Yes"),
        ("2025-09-01", 4, "turmeric_blend", "Good product. The black pepper (BioPerine) makes this more effective than standard turmeric caps. Takes about 2-3 weeks to feel results but they're real.", "Yes"),
        ("2025-10-05", 2, "turmeric_blend", "The capsules are massive. I have trouble swallowing large pills and these are definitely on the larger side. Effective but I wish they offered smaller caps or a powder option.", "Yes"),
        ("2025-08-25", 3, "turmeric_blend", "Does it have black pepper extract? The label says BioPerine which I know is black pepper but it should say that more clearly for people who aren't supplement-savvy.", "No"),
        ("2025-09-15", 4, "turmeric_blend", "Joint comfort improved after about 3 weeks of consistent use. The golden color of the capsules is reassuring — you can tell there's real turmeric in here.", "Yes"),
        ("2025-10-20", 5, "turmeric_blend", "My rheumatologist suggested trying turmeric for inflammation. These are the best I've found — proper dose, black pepper included, clean label. Joint comfort is noticeably better.", "Yes"),
        ("2025-11-02", 2, "turmeric_blend", "Great product but a bit pricey for monthly use. At $38/month it adds up. Wish there was a subscription discount like you see with the sleep gummies.", "Yes"),
        ("2025-08-18", 3, "turmeric_blend", "Capsule size is too large. I gag trying to swallow them. Otherwise a good product. Please make them smaller or offer a powder version I can mix into smoothies.", "No"),
        ("2025-09-22", 5, "turmeric_blend", "I've been taking this for 2 months. My morning stiffness has reduced significantly. Love that it has BioPerine — without it turmeric barely absorbs.", "Yes"),
        ("2025-10-28", 4, "turmeric_blend", "Clean label, no fillers, good dose of curcuminoids. Everything I look for in a turmeric supplement. The capsule is a bit big but manageable.", "Yes"),
        ("2025-11-10", 2, "turmeric_blend", "Too expensive compared to alternatives. $38 for 60 caps when you can get similar quality on Amazon for $22. The NovaBotanics branding is nice but doesn't justify the premium.", "No"),
        ("2025-09-08", 5, "turmeric_blend", "Does it have black pepper? Yes it does — BioPerine 5mg per serving. I researched this extensively. This is properly formulated. Results speak for themselves after 3 weeks.", "Yes"),
        ("2025-10-15", 3, "turmeric_blend", "Effective but the capsules are enormous. My elderly mother can't swallow them easily. Please consider a smaller capsule format or soft gels.", "Yes"),
        ("2025-11-05", 4, "turmeric_blend", "Good bioavailability with the black pepper. I've tried 5 different turmeric brands. This one and one other are the only ones that actually have enough BioPerine to matter.", "Yes"),
        ("2025-08-28", 1, "turmeric_blend", "Arrived with a broken seal. Contacted customer service and got a replacement quickly. New bottle is fine and the product seems to work but the QC issue was alarming.", "Yes"),
        ("2025-09-30", 4, "turmeric_blend", "Joint comfort improved after 3 weeks. That's the benchmark I set for myself. These passed. Reordering.", "Yes"),
        ("2025-10-10", 5, "turmeric_blend", "My fitness coach recommended these for post-workout inflammation. They work. Recovery is faster and my joints don't ache as much after heavy lifting days.", "Yes"),
        ("2025-11-18", 3, "turmeric_blend", "Pricing is a bit high for monthly use. Would love a bundle deal with the greens powder. Both products together would be $75+/month which is steep.", "No"),
        ("2025-09-05", 5, "turmeric_blend", "Been taking turmeric for 5 years. This is the best formulated one I've tried. The curcuminoid content is high and the BioPerine dose is correct (5mg minimum).", "Yes"),
        ("2025-10-22", 2, "turmeric_blend", "The capsules are uncomfortably large. I've had to start opening them and mixing the powder into food which defeats the purpose. Really wish they were smaller.", "Yes"),
        ("2025-11-12", 4, "turmeric_blend", "Good quality turmeric supplement. Black pepper extract is included which is non-negotiable for me. Slightly expensive but the quality justifies it.", "Yes"),
        ("2025-08-20", 5, "turmeric_blend", "After 3 weeks my knee inflammation is measurably better. My doctor was impressed. She asked which brand I was using and wrote it down. That's a good sign.", "Yes"),
        ("2025-09-18", 3, "turmeric_blend", "Does the job. Nothing special. Capsule size is a complaint I have too. Otherwise fine.", "No"),
        ("2025-10-30", 4, "turmeric_blend", "Solid product. Takes a few weeks to kick in but then you notice the difference. Joint comfort and morning stiffness both improved.", "Yes"),
        ("2025-11-20", 2, "turmeric_blend", "Not sure if this is working for me specifically. I've been taking it for 6 weeks with no noticeable change. May just be my body. Others clearly have good results.", "Yes"),
        ("2025-09-12", 5, "turmeric_blend", "The best turmeric I've found online. Love that the label is clean — no titanium dioxide, no artificial colors. Just turmeric and BioPerine basically.", "Yes"),
        ("2025-10-18", 4, "turmeric_blend", "Solid. Reduces my post-run soreness. I take 2 caps after long runs and notice the difference vs when I forget.", "Yes"),
        ("2025-11-08", 3, "turmeric_blend", "Pricey for monthly use but the quality is there. Wish there was a family-size or bulk option to bring the per-serving cost down.", "Yes"),
        ("2025-08-22", 5, "turmeric_blend", "Joint comfort improved, inflammation reduced. Does what it says. Reordering my third bottle.", "Yes"),
        ("2025-10-05", 3, "turmeric_blend", "Capsules are too big, monthly cost is too high. But the product works. Trade-off I'm evaluating.", "No"),
        ("2025-11-15", 4, "turmeric_blend", "Good bioavailability, clean label, decent price on subscription. Would recommend to anyone looking for a properly formulated turmeric.", "Yes"),
        ("2025-09-20", 5, "turmeric_blend", "Switched from a drugstore brand that had no black pepper extract. The difference in effectiveness is immediately obvious. This is how turmeric should be formulated.", "Yes"),
        ("2025-10-25", 2, "turmeric_blend", "Too expensive. $38/month for capsules I have trouble swallowing because they're too large. Both complaints in one product. Disappointing.", "Yes"),
        ("2025-11-01", 4, "turmeric_blend", "Strong product. Does what it promises. A bit pricey but the quality is evident. Three weeks for full effect seems accurate based on my experience.", "Yes"),
        ("2025-09-28", 5, "turmeric_blend", "My nutritionist specifically recommended this brand for the BioPerine dose and curcuminoid content. Happy with the results.", "Yes"),
    ]
    write_csv(
        BASE_DIR / "customer_voice" / "shopify_reviews_turmeric_blend.csv",
        ["date", "rating", "product", "review_text", "verified_purchase"],
        rows
    )


def gen_support_tickets():
    rows = [
        ("2025-10-01", "TKT-1001", "sleep_gummies", "shipping_issue", "My order arrived completely melted. The gummies are stuck together in one mass. Order #NB-8821.", "Reshipped with expedited shipping. Added note to include cold pack for summer orders."),
        ("2025-10-02", "TKT-1002", "sleep_gummies", "shipping_issue", "Ordered last week and gummies melted in transit. This is the second time this has happened in summer. Please fix the packaging.", "Reshipped. Customer flagged as repeat shipping issue. Escalated to ops team."),
        ("2025-10-05", "TKT-1003", "turmeric_blend", "product_question", "Does your turmeric have black pepper extract? The label says BioPerine but I want to confirm that's black pepper.", "Confirmed BioPerine is black pepper extract (Piper nigrum). Each serving contains 5mg."),
        ("2025-10-06", "TKT-1004", "sleep_gummies", "subscription_management", "I need to pause my subscription for 2 months while I travel. How do I do this?", "Provided instructions to pause via account portal. Paused subscription per customer request."),
        ("2025-10-07", "TKT-1005", "greens_powder", "product_question", "Is your greens powder third-party tested? I need to know before I can take it (competitive athlete).", "Confirmed NSF Sport certified. Shared COA link. Customer satisfied."),
        ("2025-10-08", "TKT-1006", "turmeric_blend", "refund_request", "Capsules are too large for me to swallow. I've opened 3 so far. Would like a refund for the rest of the bottle.", "Issued full refund. Noted feedback on capsule size for product team."),
        ("2025-10-09", "TKT-1007", "sleep_gummies", "shipping_issue", "Package says delivered but I don't have it. Order #NB-9042.", "Investigated with carrier. Package confirmed lost. Reshipped at no charge."),
        ("2025-10-10", "TKT-1008", "magnesium", "product_question", "What's the difference between your magnesium and glycinate vs citrate? Which form is in yours?", "Confirmed magnesium glycinate bisglycinate chelate. Explained better absorption vs oxide/citrate."),
        ("2025-10-12", "TKT-1009", "sleep_gummies", "subscription_management", "Subscription was cancelled without my permission. I did not cancel it. Running out of gummies.", "Found system error cancelled subscription during platform migration. Reinstated immediately. Apologized and sent 1-month free."),
        ("2025-10-13", "TKT-1010", "turmeric_blend", "product_question", "How long before I notice results from the turmeric? I've been taking it for 1 week with no change.", "Advised typical onset 2-4 weeks with consistent daily use. Recommended taking with food for best absorption."),
        ("2025-10-14", "TKT-1011", "sleep_gummies", "product_quality", "Gummies taste artificial and too sweet. The last batch tasted different from the previous order.", "Checked batch number. Product team confirmed minor flavoring adjustment. Offered replacement from prior formulation batch."),
        ("2025-10-15", "TKT-1012", "greens_powder", "shipping_issue", "Powder arrived with a broken seal. Lid was cracked. Powder was exposed.", "Reshipped immediately. Flagged packaging supplier for cracked lid issue."),
        ("2025-10-17", "TKT-1013", "sleep_gummies", "refund_request", "Product didn't work for me after 3 weeks. Requesting refund under your guarantee.", "Issued full refund per 30-day guarantee. Noted non-responder in CRM."),
        ("2025-10-18", "TKT-1014", "turmeric_blend", "shipping_issue", "Order says arriving today but tracking hasn't updated in 5 days.", "Investigated. Carrier delay. Updated tracking shared. Order arrived 2 days later."),
        ("2025-10-20", "TKT-1015", "sleep_gummies", "product_question", "What changed in the new formula? I noticed the gummies taste slightly different.", "Explained reformulation: melatonin reduced from 5mg to 3mg, L-theanine 100mg added. Customers reporting less grogginess."),
        ("2025-10-21", "TKT-1016", "magnesium", "subscription_management", "Need to change subscription frequency from monthly to every 45 days. I'm not going through it fast enough.", "Updated subscription cadence to 45 days per request."),
        ("2025-10-22", "TKT-1017", "sleep_gummies", "shipping_issue", "Gummies melted again. Third time in summer months. Are you going to fix this?", "Escalated to ops. Expedited reship with cold pack. Flagged for summer packaging initiative."),
        ("2025-10-24", "TKT-1018", "greens_powder", "product_question", "Can I mix the greens powder with my protein shake or will it affect the taste significantly?", "Confirmed mixable. Suggested blending with smoothies for best taste. Provided recipe suggestions."),
        ("2025-10-25", "TKT-1019", "turmeric_blend", "refund_request", "The capsules are too big. I tried for a week but I can't get them down easily. Want a refund.", "Issued full refund. Capsule size feedback added to product backlog."),
        ("2025-10-27", "TKT-1020", "sleep_gummies", "subscription_management", "How do I add a second product to my subscription? Want to add turmeric.", "Provided instructions to add second subscription in account portal. Offered bundle discount."),
        ("2025-10-28", "TKT-1021", "magnesium", "product_quality", "Capsules have a slight smell that seems off. Should magnesium smell like this?", "Confirmed normal — magnesium glycinate has a slight characteristic smell. Not indicative of quality issue. Provided COA."),
        ("2025-10-30", "TKT-1022", "sleep_gummies", "product_question", "Can I take these with melatonin I already have or is that too much melatonin combined?", "Advised not to double up on melatonin sources. Recommended using just NovaBotanics gummies which contain 3mg melatonin."),
        ("2025-11-01", "TKT-1023", "turmeric_blend", "shipping_issue", "Ordered 2 bottles. Only 1 arrived. Packing slip shows 2.", "Investigated. Second bottle was misscanned. Located and expedited. Delivered within 2 days."),
        ("2025-11-03", "TKT-1024", "sleep_gummies", "product_quality", "Gummies are extremely sticky and hard to separate. Some are stuck to the bottle.", "Noted batch number. Confirmed humidity issue in that production run. Reshipped from newer batch."),
        ("2025-11-05", "TKT-1025", "greens_powder", "refund_request", "The taste is just too much for me. Too earthy. Can't get it down even in a smoothie.", "Issued refund. Suggested trying a flavored version if we launch one. Noted taste feedback."),
        ("2025-11-07", "TKT-1026", "sleep_gummies", "subscription_management", "Want to cancel subscription. Moving abroad and can't get international shipping.", "Cancelled per request. Offered to hold and resume when returns. Customer noted they'd come back."),
        ("2025-11-10", "TKT-1027", "turmeric_blend", "product_question", "Is this suitable for someone on blood thinners? My doctor asked.", "Advised customer to consult their prescribing physician. Noted turmeric can interact with blood thinners. Did not make medical recommendation."),
        ("2025-11-12", "TKT-1028", "magnesium", "product_question", "When is the best time to take magnesium? Morning or night?", "Advised most customers take with dinner or before bed as magnesium glycinate can be calming. Morning also fine for general mineral support."),
    ]
    write_csv(
        BASE_DIR / "customer_voice" / "support_tickets_q4_2025.csv",
        ["date", "ticket_id", "product", "category", "customer_message", "resolution"],
        rows
    )


def gen_social_mentions():
    content = """NovaBotanics Social Mentions Compiled - Q4 2025
Source: Instagram, TikTok, Reddit (r/supplements, r/sleep)
Compiled: November 2025
================================================

INSTAGRAM
---------
@wellness_with_maya: Just started NovaBotanics sleep gummies and I'm actually sleeping through the night??? The L-theanine is the secret ingredient no one talks about. #sleepgummies #novabotanics

@theguthealthguy: Tried the NovaBotanics turmeric blend for 3 weeks. Joint comfort is real. The BioPerine makes all the difference for absorption. Legit product.

@fitmomsunite: My kids keep asking why mommy's gummies are off limits lol. The NovaBotanics sleep gummies are MINE. Best purchase of the month.

@cleanlabeobsessed: Finally a supplement brand that doesn't sneak in titanium dioxide or artificial colors. NovaBotanics check all my clean label boxes. @novabotanics thank you.

@supplementskeptic: OK I was skeptical about NovaBotanics but 30 days in — the turmeric blend is working. Morning stiffness down noticeably. Giving credit where it's due.

@momofthree_wellness: Does NovaBotanics ship internationally? Asking for my sister in Canada. Would love to send her the sleep gummies.

@brendan.lifts: Using the magnesium before bed + sleep gummies combo. Deepest sleep I've had since college. Recovery is noticeably better.

@herbalfoodie: The NovaBotanics greens powder mixed into my morning smoothie. Low key delicious if you do it right. Key is ice + banana to cut the earthiness.

@simplywholeness: NovaBotanics just hit my top 5 supplement brands. Clean ingredients, no BS, actually works. The sleep gummies have a berry flavor? No? Please make one.

@sleeptrackernerds: Tracked my sleep with Oura ring before and after NovaBotanics gummies. Deep sleep up 18 minutes average. Correlation not causation but still notable.

TIKTOK
------
@dr.sleepwell: Reviewing NovaBotanics sleep gummies for my followers. The 3mg melatonin + 100mg L-theanine combo is clinically reasonable. Not too much melatonin which is a common industry mistake. Worth trying. [42K views]

@novabotanicsfan: POV you find a supplement brand with no fillers, no artificial flavors, and it actually works. NovaBotanics sleep gummies. That's the video. [18K views]

@supplementreviewer2025: Comparing NovaBotanics vs ZenLeaf sleep gummies side by side. NovaBotanics wins on ingredient quality. ZenLeaf wins on price. Depends on your priorities. [31K views]

@tired_no_more: 30 day NovaBotanics sleep gummy challenge complete. Results: fell asleep faster in 24 of 30 days. Worth it. The L-theanine is the differentiator vs other brands. [9K views]

@gelicahealth: Please NovaBotanics make a berry flavor!! The mango is fine but berry would be amazing!! Who agrees?? [6K views, 247 comments "BERRY!"]

REDDIT (r/supplements)
----------------------
u/sleepoptimizer99: Has anyone compared NovaBotanics to ZenLeaf for sleep? Considering switching. NovaBotanics seems cleaner but ZenLeaf is cheaper.
> u/insomniac_reformed: Made that switch 2 months ago. NovaBotanics is meaningfully better. The lower melatonin is key — I was getting rebound insomnia from ZenLeaf's 5mg dose.
> u/supplement_nerd_pdx: Agree. NovaBotanics formulation is better. Pay the extra $5, worth it.

u/inflamedjoints: Anyone tried NovaBotanics turmeric for joint inflammation? My sports doc suggested it.
> u/runnersknee_fixed: 4 weeks in. My knee inflammation is noticeably better. The BioPerine dose is correct which a lot of brands cheap out on. Recommend.
> u/skeptic_but_curious: How long before it works? I've seen 2-4 weeks mentioned.

REDDIT (r/sleep)
----------------
u/can_never_sleep: NovaBotanics sleep gummies are the first sleep supplement that doesn't make me feel hungover the next morning. The lower melatonin + L-theanine combo is the reason why. If you've had morning grogginess from other sleep supplements, try these.

u/newmom_exhausted: Desperate for sleep help. Are the NovaBotanics gummies safe while breastfeeding?
> u/mod_r_sleep: [Mod] Please consult your OB/GYN. We can't give medical advice here.
> u/newmom_exhausted: Of course, I'll ask my doctor. Just looking for real user experiences.

u/gummy_vitamin_fan: The NovaBotanics mango flavor is fine but I'd really love a berry option. They should survey their customers on this. I've seen the request in Amazon reviews too.
"""
    write_txt(BASE_DIR / "customer_voice" / "social_mentions_compiled.txt", content)


# ─────────────────────────────────────────────
# WORKSPACE 2: TEAM BRAIN
# ─────────────────────────────────────────────

def gen_brand_guidelines():
    content = """NOVABOTANICS BRAND GUIDELINES
Version 2.1 | Updated October 2025
====================================

1. BRAND OVERVIEW
-----------------
NovaBotanics is a D2C wellness supplement brand built on the belief that clean, science-backed
supplements shouldn't require a biochemistry degree to understand. We serve health-conscious
adults who want supplements that actually work — without unnecessary fillers, proprietary blends,
or misleading claims.

Tagline: "Science you can read. Supplements you can trust."

2. BRAND VOICE
--------------
Core Personality Traits:
  - Warm but not fluffy
  - Science-backed but not clinical or cold
  - Approachable but not dumbed-down
  - Direct but not harsh
  - Confident but never arrogant

Voice Do's:
  - Use plain English. If you need a glossary to understand our label, we've failed.
  - Reference the science when it matters. Cite mechanisms, not just outcomes.
  - Acknowledge complexity. "This takes 2-4 weeks to work and here's why" beats "miracle results!"
  - Show empathy for the customer's actual problem (poor sleep, joint pain, low energy).
  - Use "you" and "your" to speak directly to the customer.

Voice Don'ts:
  - No exclamation point overload. One per paragraph maximum.
  - No miracle claims or language that implies guaranteed outcomes.
  - No "proprietary blend" language — we disclose all ingredient amounts.
  - No fear-mongering about other brands.
  - No filler adjectives: "amazing," "incredible," "revolutionary" without substance behind them.
  - Never say "all-natural" — it's meaningless and often inaccurate.
  - Never imply medical treatment or claim to diagnose, cure, treat, or prevent any disease.

3. SOCIAL MEDIA DO'S AND DON'TS
---------------------------------
DO:
  - Post ingredient spotlights explaining what an ingredient does and why we included it
  - Share customer stories (with permission) — real results from real people
  - Explain formulation decisions ("We use 3mg melatonin, not 10mg, because here's the science")
  - Use before/after sleep quality data from customers (Oura ring, sleep trackers)
  - Post behind-the-scenes: manufacturing, testing, quality standards
  - Engage with supplement science conversations in the comments
  - Respond to every question about ingredients with a real answer

DON'T:
  - Repost influencer content that makes health claims we can't substantiate
  - Post anything that implies our products cure or treat any health condition
  - Use stock imagery of airbrushed people — use real customers and real team members
  - Post price comparisons that disparage competitor products by name
  - Ghost negative comments — always respond constructively

4. VISUAL IDENTITY
------------------
Primary Colors:
  - Forest Green: #2D5016 (primary brand color, used for logo and primary CTAs)
  - Warm White: #F8F5F0 (backgrounds)
  - Gold Accent: #C9A84C (accents, highlighting key data)

Typography:
  - Headlines: Freight Display Pro (serif — approachable authority)
  - Body: Inter (clean, readable at small sizes)
  - Data/labels: Roboto Mono (clinical credibility for ingredient amounts)

Photography Style:
  - Bright, airy, natural light preferred
  - Real environments (kitchen counter, nightstand, gym bag) over studio backdrops
  - Ingredients shown in their raw form alongside finished product
  - People shown in real moments, not posed perfection

5. PACKAGING LANGUAGE STANDARDS
--------------------------------
Supplement Facts Panel:
  - All ingredient amounts must be disclosed — no "proprietary blend"
  - Include the source form of each ingredient (e.g., "Magnesium (as magnesium glycinate bisglycinate chelate)")
  - Include the form of curcumin and confirmation of BioPerine for turmeric products

Front Panel:
  - Claim hierarchy: Primary benefit claim → Key ingredient → Key differentiator
  - Example: "Sleep Support | Melatonin + L-Theanine | No Artificial Colors"
  - No asterisk-buried claims on the front — if it needs a footnote, it shouldn't be there

6. CUSTOMER COMMUNICATION STANDARDS
--------------------------------------
Email:
  - Respond within 24 hours
  - No templates that don't acknowledge the specific issue
  - When we're wrong, say so directly and fix it

Refunds:
  - 30-day satisfaction guarantee, no questions asked
  - Process within 3 business days

7. THINGS THAT DEFINE US
--------------------------
Non-negotiables (things we will never compromise on):
  - Full ingredient disclosure on every product
  - Third-party testing for every batch
  - No ingredients we can't explain and justify
  - Honest marketing — no claims we can't back with evidence or customer data
"""
    write_txt(BASE_DIR / "team_brain" / "NovaBotanics_Brand_Guidelines.txt", content)


def gen_sop_launch():
    content = """STANDARD OPERATING PROCEDURE: NEW PRODUCT LAUNCH
NovaBotanics Internal SOP v1.4
Last Updated: September 2025
================================================

PURPOSE
-------
This SOP defines the 12-week process for launching a new supplement product at NovaBotanics.
All product launches must follow this process. Deviations require VP approval and must be
documented in the launch record.

WEEK-BY-WEEK TIMELINE
----------------------

WEEK 1-2: CONCEPT VALIDATION
  Owner: Product Team
  Tasks:
    [ ] Define product concept, target customer problem, and differentiation hypothesis
    [ ] Review customer voice data (reviews, support tickets) for demand signals
    [ ] Competitive analysis: identify top 5 competitors, their formulations, price points
    [ ] Define formulation requirements: key actives, doses, delivery format
    [ ] Present concept brief to leadership for green light
  Deliverable: Approved concept brief signed by VP Product

WEEK 3-4: FORMULATION DEVELOPMENT
  Owner: Product Team + Formulation Consultant
  Tasks:
    [ ] Work with formulation consultant to develop initial formula
    [ ] Source ingredient candidates from approved supplier list
    [ ] Request COAs and spec sheets from shortlisted suppliers
    [ ] Confirm third-party testing requirements (NSF, Informed Sport, etc.)
    [ ] Build cost model at target MOQs
  Deliverable: Approved formula + preliminary cost model

WEEK 5-6: REGULATORY & COMPLIANCE REVIEW
  Owner: Compliance Lead
  Tasks:
    [ ] Review formula for any ingredients requiring special labeling
    [ ] Draft supplement facts panel per FDA 21 CFR Part 101 requirements
    [ ] Review all planned marketing claims against FTC/FDA guidelines
    [ ] Confirm no health claims that imply disease treatment without structure/function language
    [ ] Legal review of final label copy
  Deliverable: Compliance-cleared label copy

WEEK 7-8: SUPPLIER FINALIZATION & PRODUCTION PREP
  Owner: Operations + Product
  Tasks:
    [ ] Finalize supplier selection (primary + backup)
    [ ] Place sample/pilot production order
    [ ] Receive and evaluate pilot samples (taste, texture, appearance, potency)
    [ ] Approve final packaging design with brand guidelines compliance check
    [ ] Set up SKUs in Shopify and inventory management system
  Deliverable: Approved pilot samples, production order placed

WEEK 9-10: MARKETING PREPARATION
  Owner: Marketing Team
  Tasks:
    [ ] Write all product copy: PDP, email, social, paid ad copy (brand voice compliant)
    [ ] Shoot product photography and lifestyle imagery
    [ ] Create ingredient explainer content (social, email sequence)
    [ ] Build pre-launch email list and lead capture page
    [ ] Brief influencer/affiliate partners (no health claims in briefs)
    [ ] Create FAQ document for customer service team
  Deliverable: All launch assets created and approved

WEEK 11: PRE-LAUNCH TESTING
  Owner: All Teams
  Tasks:
    [ ] Full website QA: product page, checkout, email flows
    [ ] Customer service team briefed on product FAQs and common objections
    [ ] Inventory confirmed in warehouse with buffer stock
    [ ] Test subscription setup if applicable
    [ ] Internal soft launch: team members try product and provide feedback
  Deliverable: Launch readiness checklist completed and signed off

WEEK 12: LAUNCH
  Owner: Marketing + Ops
  Tasks:
    [ ] Launch day: activate all marketing channels simultaneously
    [ ] Monitor inventory levels hourly for first 48 hours
    [ ] Monitor customer service inbox for early questions/issues
    [ ] Post-launch check at 24 hours, 48 hours, 1 week
    [ ] Capture launch metrics: conversion rate, AOV, email open rates, early reviews
  Deliverable: Launch metrics report at Day 7

POST-LAUNCH: 30-DAY REVIEW
  Tasks:
    [ ] Collect and analyze first 30 days of customer reviews
    [ ] Review support ticket categories for unexpected issues
    [ ] Adjust FAQ and CS scripts based on real customer questions
    [ ] First reorder trigger: place replenishment order at 50% inventory remaining
    [ ] Evaluate launch performance vs targets; document learnings

APPROVAL REQUIREMENTS
---------------------
The following require explicit sign-off before proceeding:
  - Concept brief → VP Product
  - Formula finalization → Product Lead + Formulation Consultant
  - Label copy → Compliance Lead + Legal
  - Production order → COO (orders >$25K require CEO sign-off)
  - Launch go/no-go → VP Marketing + COO

ESCALATION
----------
If any milestone is missed by more than 5 business days, escalate to COO immediately.
Do not delay launch without explicit executive decision.
"""
    write_txt(BASE_DIR / "team_brain" / "SOP_New_Product_Launch.txt", content)


def gen_meeting_notes():
    content = """MEETING NOTES: Q4 2025 PRODUCT PLANNING
Date: October 8, 2025
Location: Conference Room B + Zoom
Attendees: Jordan (CEO), Priya (VP Product), Marcus (Formulation Consultant), Leah (Marketing Lead), Sam (Operations)
Note-taker: Leah
================================================

AGENDA ITEMS
------------

1. Sleep Gummies Reformulation: Final Decision

Background: The original sleep gummy formula launched in January 2024 contained 5mg melatonin
and no other sleep-support actives. Over 18 months, a consistent pattern emerged in customer
reviews and support tickets: morning grogginess. Approximately 23% of reviewer comments
referenced feeling foggy, groggy, or oversedated the next morning. The 5mg melatonin dose
was identified as the likely culprit by our formulation consultant.

Marcus (consultant) presented three options:
  Option A: Reduce melatonin to 3mg, no other changes
  Option B: Reduce melatonin to 3mg, add L-theanine 100mg
  Option C: Remove melatonin entirely, build formula around L-theanine + glycine + magnesium

Discussion:
  - Jordan: "Option C is interesting long-term but represents a positioning shift. We need
    continuity with our existing customer base who chose us for melatonin support."
  - Priya: "The evidence for L-theanine + melatonin combination is strong. L-theanine reduces
    sleep latency (time to fall asleep) while melatonin supports circadian timing. Lower melatonin
    reduces morning grogginess while L-theanine compensates with calming effect."
  - Leah: "From a marketing angle, Option B gives us a reformulation story we can tell. 'We
    listened to your feedback and made it better.' That's compelling content."
  - Sam: "Option B requires sourcing L-theanine from our supplier list. PurePlant carries it.
    Lead time is 45 days. We'd need to build buffer stock before the switch."

DECISION: Option B approved unanimously.
  - Melatonin: reduced from 5mg to 3mg
  - L-theanine: added at 100mg (Suntheanine brand, for standardization)
  - All other ingredients unchanged
  - Target launch of reformulated product: January 2026

ACTION ITEMS:
  [ ] Marcus: finalize new formula specification by Oct 15
  [ ] Sam: confirm PurePlant lead time and place L-theanine order
  [ ] Priya: update product roadmap with reformulation timeline
  [ ] Leah: draft reformulation announcement email for existing customers

---

2. Q1 2026 New Product: Candidate Review

Three candidates were presented for Q1 2026 launch. Team voted on priorities.

Candidate A: Ashwagandha Stress Supplement (KSM-66 extract)
  - Market: stress/cortisol management is top-3 wellness search category
  - Competitive gap: most competitors use non-standardized ashwagandha. KSM-66 is the
    gold standard but most D2C brands use cheaper generic extract.
  - Supplier: SupplierA (PurePlant) already carries KSM-66, strong COA on file
  - Vote: 4/5 in favor

Candidate B: Sleep Support 2.0 (melatonin-free, L-theanine + glycine + magnesium)
  - Market: growing segment of customers who don't want melatonin
  - Competitive gap: most sleep products still melatonin-heavy
  - Risk: cannibalizes existing sleep gummy line
  - Vote: 2/5 in favor (tabled for Q3 2026)

Candidate C: Collagen + Vitamin C (marine collagen, skin/joint support)
  - Market: massive and growing but highly competitive
  - Risk: doesn't align with our science-backed/clinical positioning
  - Vote: 1/5 in favor (removed from roadmap)

DECISION: Q1 2026 new product launch = Ashwagandha (KSM-66). Marcus to begin formulation.

---

3. Pricing Review: Subscription Discount Structure

Current: 15% subscription discount across all products
Proposal: Tiered structure based on bundle size

Proposed tiers:
  Single product subscription: 15% off (unchanged)
  2-product bundle subscription: 20% off
  3+ product bundle subscription: 25% off

Rationale: Increase LTV by incentivizing multi-product households. Current AOV for
subscription customers is $38 (single product). Target AOV is $65+.

Decision: Approved. Leah to update pricing page and email sequences. Sam to update
Shopify discount rules. Target implementation: November 1, 2025.

---

NEXT MEETING
------------
Date: November 12, 2025
Agenda: L-theanine supplier confirmation, ashwagandha formulation update, Q4 holiday
campaign review
"""
    write_txt(BASE_DIR / "team_brain" / "Meeting_Notes_Q4_Product_Planning.txt", content)


def gen_onboarding():
    content = """NOVABOTANICS EMPLOYEE ONBOARDING: PRODUCT KNOWLEDGE GUIDE
For New Team Members | Updated November 2025
================================================

WELCOME
-------
This guide gives you everything you need to understand our product line, answer customer
questions, and represent NovaBotanics accurately. Read this in your first week.

THE PRODUCT LINE
----------------

1. SLEEP GUMMIES (Reformulated January 2026)
   Format: Gummies (mango flavor, 60 count)
   Serving: 2 gummies, 30 min before bed
   Key Ingredients:
     - Melatonin 3mg: regulates circadian rhythm, helps with sleep onset
     - L-Theanine 100mg (Suntheanine): promotes calm alertness, reduces sleep latency,
       improves sleep quality without sedation
   Why we changed it: Original formula had 5mg melatonin, causing morning grogginess in
   ~23% of users. We reduced melatonin and added L-theanine based on customer feedback
   and formulation review. Current formula is the best version we've made.
   Differentiators vs competitors:
     - Lower melatonin dose (most competitors use 5-10mg — too much)
     - L-theanine addition (most sleep gummies skip this)
     - Clean label: no artificial colors, no corn syrup
   Price: $34 one-time | $28.90/month (15% subscription discount)
   Common customer questions:
     - "Will I feel groggy?" → Much less likely with 3mg melatonin. L-theanine improves
       sleep quality without heavy sedation.
     - "When will I feel results?" → Most customers notice improvement by night 2-3.
     - "Can I take with other supplements?" → Yes for most. Advise against doubling up
       on melatonin from other sources.

2. TURMERIC BLEND
   Format: Capsules (60 count)
   Serving: 2 capsules daily with food
   Key Ingredients:
     - Turmeric Extract 500mg (95% curcuminoids): anti-inflammatory, joint support
     - BioPerine 5mg (black pepper extract): increases curcumin absorption by up to 2000%
   Why the BioPerine matters: Curcumin has famously poor bioavailability. Without a
   bioavailability enhancer, most of it passes through unabsorbed. BioPerine is the
   clinical standard. Many competitors skip it or underdose it (need minimum 5mg).
   Differentiators: Proper BioPerine dose, 95% curcuminoid standardization, no fillers
   Price: $38 one-time | $32.30/month subscription
   Common customer questions:
     - "How long to feel results?" → Typically 2-4 weeks of consistent daily use
     - "Does it have black pepper?" → Yes, BioPerine = black pepper extract. 5mg per serving.
     - "Capsule is too big" → Known issue. Collecting feedback for next batch consideration.

3. DAILY GREENS POWDER
   Format: Powder (30 servings)
   Serving: 1 scoop in 8-16oz water or smoothie
   Key Ingredients:
     - Organic greens blend: spirulina, chlorella, barley grass, wheatgrass
     - Digestive enzyme blend: protease, amylase, lipase, cellulase
     - Probiotic blend: 5 billion CFU, 8 strains
   Certifications: NSF Sport certified (safe for athletes, tested for banned substances)
   Taste: Earthy-green. Best masked in a smoothie with banana and ice.
   Price: $45 one-time | $38.25/month subscription
   Common questions:
     - "Is it safe for athletes?" → Yes, NSF Sport certified.
     - "Does it taste bad?" → It's earthy. Smoothie recommended. Honest answer.

4. MAGNESIUM SUPPLEMENT
   Format: Capsules (90 count)
   Serving: 2 capsules (200mg elemental magnesium) with dinner or before bed
   Key Ingredient: Magnesium glycinate bisglycinate chelate
   Why this form: Magnesium oxide is cheap and poorly absorbed (~4%). Magnesium glycinate
   is highly bioavailable (~80%) and gentler on digestion. Bisglycinate chelate is the
   premium form.
   Common use cases: Sleep quality, muscle recovery, stress response, general mineral support
   Price: $28 one-time | $23.80/month subscription

FREQUENTLY ASKED NEW HIRE QUESTIONS
--------------------------------------
Q: Why don't we sell on Amazon?
A: We currently sell D2C only through Shopify. Amazon is under evaluation for 2026 but we
   want to maintain customer relationship and data ownership first.

Q: What's our return/refund policy?
A: 30-day satisfaction guarantee. Full refund, no questions asked. Process within 3 business days.

Q: How do we handle medical questions?
A: We do not provide medical advice. Always advise customers to consult their healthcare provider
   for medical decisions. We can share product facts and our COAs.

Q: Who handles customer service?
A: CS team (Sarah, Mike, Tanvir). Escalate anything involving a health reaction or legal threat
   immediately to your manager.
"""
    write_txt(BASE_DIR / "team_brain" / "Employee_Onboarding_Product_Knowledge.txt", content)


def gen_pricing_strategy():
    content = """NOVABOTANICS PRICING STRATEGY 2026
INTERNAL DOCUMENT — CONFIDENTIAL
Last Updated: November 2025
================================================

1. PRICING PHILOSOPHY
---------------------
We price for perceived value, not commodity competition. Our customers pay a premium for:
  - Clean label (no fillers, full ingredient disclosure)
  - Third-party testing
  - Clinically-dosed active ingredients
  - Transparent brand communication

We do not compete on price with Amazon warehouse brands. We compete on trust and quality.
Price anchoring is against the highest quality D2C brands (AG1, Ritual), not drugstore brands.

2. CURRENT PRODUCT PRICING
---------------------------
Product              | MSRP    | Sub Price | COGS   | Gross Margin | Sub Margin
Sleep Gummies (60ct) | $34.00  | $28.90    | $8.20  | 75.9%        | 71.7%
Turmeric Blend (60ct)| $38.00  | $32.30    | $9.50  | 75.0%        | 70.6%
Greens Powder (30sv) | $45.00  | $38.25    | $11.80 | 73.8%        | 69.2%
Magnesium (90ct)     | $28.00  | $23.80    | $6.40  | 77.1%        | 72.9%

Target gross margin: 70%+ across all products. Current portfolio average: 75.4%.

3. SUBSCRIPTION DISCOUNT STRUCTURE (Effective November 1, 2025)
----------------------------------------------------------------
Single product: 15% off MSRP
2-product bundle: 20% off MSRP (new)
3+ product bundle: 25% off MSRP (new)

Rationale: Multi-product households have 3x higher LTV. Bundle incentive is designed to
increase subscription AOV from current $38 toward $65+ target.

Operational note: Bundles are configured in Shopify as subscription groups. Sam to confirm
Recharge configuration is live by November 1.

4. WHOLESALE / RETAIL PRICING (For Future Consideration)
---------------------------------------------------------
We do not currently sell wholesale. If/when we pursue retail:
  - Wholesale price: 50% of MSRP
  - Minimum viable retail margin: 40% for retailer
  - Retail MSRP must match or exceed D2C MSRP (MAP policy)
  - Minimum order: 24 units per SKU

No retail deals to be negotiated without VP and CEO approval.

5. PROMOTIONAL CALENDAR
------------------------
We run 4 major promotions per year:
  - New Year (January 2): 20% off sitewide — New Year wellness positioning
  - Spring Launch (April): New product launch discount — 25% off new SKU for first 72 hours
  - Back to School (August): 15% off storewide — routine-building messaging
  - Black Friday/Cyber Monday (November): 25% off sitewide, max discount of the year

We do NOT run ad-hoc flash sales. Constant discounting trains customers to wait for deals
and devalues the brand.

6. BUNDLE PRODUCTS (2026 Roadmap)
-----------------------------------
Planned bundles for H1 2026:
  - Sleep Stack: Sleep Gummies + Magnesium ($55, saves $7 vs individual)
  - Wellness Foundation: Greens + Magnesium + Turmeric ($95, saves $16 vs individual)

Bundles serve dual purpose: increase AOV and introduce customers to multiple products.
Analysis shows customers who use 3+ products have 85% lower churn than single-product users.

7. NEW PRODUCT PRICING: ASHWAGANDHA (Q1 2026)
----------------------------------------------
Preliminary pricing:
  - MSRP target: $36
  - Sub price: $30.60 (15% discount)
  - Target COGS: $8.50 (KSM-66 is premium ingredient — higher COGS than standard ashwagandha)
  - Target gross margin: 76.4%

Competitive reference:
  - KSM-66 products in market range: $24-45
  - Our positioning: mid-premium ($36) justified by KSM-66 standardization vs generic extract

Pricing subject to final COGS confirmation from Marcus and Sam once supplier order placed.
"""
    write_txt(BASE_DIR / "team_brain" / "Pricing_Strategy_2026.txt", content)


# ─────────────────────────────────────────────
# WORKSPACE 3: COMPETITOR INTEL
# ─────────────────────────────────────────────

def gen_competitor_analysis():
    content = """COMPETITOR ANALYSIS: SLEEP SUPPLEMENT CATEGORY
NovaBotanics Internal Research | Updated October 2025
================================================

OVERVIEW
--------
The sleep supplement market is crowded but poorly differentiated. Most products use
high-dose melatonin (5-10mg) which drives short-term sales but long-term customer
churn due to grogginess side effects. Opportunity exists for science-backed, lower-dose
formulations with additional sleep-support actives.

COMPETITOR COMPARISON TABLE
-----------------------------

Brand: ZenLeaf Sleep Support
  Format: Gummies
  Key Ingredients: Melatonin 5mg, Chamomile 25mg
  Price Per Serving: $0.48 ($28.99/60ct)
  Amazon Rating: 4.1/5 (3,847 reviews)
  Differentiators: Low price, widely available, Prime shipping
  Weaknesses: High melatonin (grogginess complaints in reviews), artificial colors (Red 40, Blue 1),
    no L-theanine or other synergistic actives
  Recurring Review Themes: "Works but groggy in morning" / "Price is great" / "Artificial taste"

Brand: MoonRest Premium Sleep
  Format: Gummies
  Key Ingredients: Melatonin 10mg, L-Theanine 200mg, Magnesium 50mg
  Price Per Serving: $0.90 ($53.99/60ct)
  Amazon Rating: 4.4/5 (1,203 reviews)
  Differentiators: Premium positioning, high L-theanine dose, magnesium addition
  Weaknesses: Very high melatonin (10mg — well above clinical recommendation), premium price,
    proprietary blend (doesn't disclose individual amounts fully)
  Recurring Review Themes: "Premium quality" / "Too expensive" / "10mg melatonin is too much for me"

Brand: NightCalm Sleep Aid
  Format: Capsules
  Key Ingredients: Melatonin 3mg, Valerian Root 500mg, Passionflower 250mg
  Price Per Serving: $0.33 ($19.99/60ct)
  Amazon Rating: 3.9/5 (2,156 reviews)
  Differentiators: Multi-herb formula, lowest price point, capsule format
  Weaknesses: Herbal ingredients have mixed evidence (valerian in particular), no L-theanine,
    capsule format less appealing than gummies, dated branding
  Recurring Review Themes: "Affordable" / "Herbal taste is strong" / "Inconsistent effects"

Brand: DreamWell Sleep Gummies
  Format: Gummies
  Key Ingredients: Melatonin 5mg, GABA 100mg, L-Theanine 100mg
  Price Per Serving: $0.70 ($41.99/60ct)
  Amazon Rating: 4.3/5 (892 reviews)
  Differentiators: GABA addition (trendy), decent L-theanine dose, modern branding
  Weaknesses: GABA supplementation has poor blood-brain barrier crossing (limited evidence),
    5mg melatonin still high, price premium without clean label
  Recurring Review Themes: "Modern branding" / "GABA doesn't seem to do much" / "Good sleep, some grogginess"

Brand: RestEasy Natural Sleep
  Format: Softgels
  Key Ingredients: Melatonin 2.5mg, Ashwagandha (KSM-66) 300mg, L-Theanine 100mg
  Price Per Serving: $0.83 ($49.99/60ct)
  Amazon Rating: 4.2/5 (567 reviews)
  Differentiators: KSM-66 ashwagandha (premium), low melatonin, multi-modal approach
  Weaknesses: Softgel format vs gummy preference, lower review volume, premium price,
    less brand awareness
  Recurring Review Themes: "Best clean formula I've found" / "Too expensive" / "Wish it were gummies"

NOVABOTANICS POSITIONING SUMMARY
---------------------------------
Vs ZenLeaf: We win on ingredient quality (no artificial colors, L-theanine, lower melatonin).
  They win on price. Key differentiation message: "Spend $6 more, wake up without grogginess."

Vs MoonRest: We win on melatonin dosing (3mg vs 10mg) and price ($34 vs $54).
  They win on review volume and premium brand awareness.

Vs NightCalm: We win significantly on evidence base (L-theanine vs herbal blends), format, and branding.
  They win on price. Not our direct competitor — different customer.

Vs DreamWell: We win on clean label and formulation (lower melatonin, L-theanine vs GABA).
  Similar price point. Main battleground: brand trust and ingredient transparency.

Vs RestEasy: Most similar formula philosophy. We win on gummy format preference.
  Price is comparable. This is our closest true competitor.

PRICING POSITION
----------------
Competitor range: $0.33 - $0.90 per serving
NovaBotanics: $0.57 per serving (one-time) / $0.48 per serving (subscription)
Position: Mid-premium, well-justified by clean label and L-theanine inclusion.

OPPORTUNITY GAPS IDENTIFIED
-----------------------------
1. Berry flavor: Multiple competitor products offer berry (ZenLeaf has "Mixed Berry" SKU).
   We have mango only. Customer demand signal is present in our own reviews.
2. Melatonin-free segment: Growing consumer preference for melatonin-free sleep support.
   No major player has a gummy in this format yet. RestEasy is closest in positioning.
3. Children's sleep segment: Not our current market, but adjacent.
4. Subscription bundles: Most competitors are single-product. We have bundle opportunity.
"""
    write_txt(BASE_DIR / "competitor_intel" / "Competitor_Analysis_Sleep_Category.txt", content)


def gen_market_trends():
    content = """MARKET TRENDS: WELLNESS SUPPLEMENT INDUSTRY 2026
NovaBotanics Internal Research | Q4 2025
================================================

EXECUTIVE SUMMARY
-----------------
The global dietary supplement market reached $177B in 2025, growing at 8.6% CAGR.
D2C supplement brands now account for 31% of market share, up from 18% in 2020.
Key growth drivers: post-pandemic health awareness, aging demographics, clean label movement,
personalization technology, and functional ingredient innovation.

TOP 10 TRENDS RELEVANT TO NOVABOTANICS
----------------------------------------

1. CLEAN LABEL IS NOW TABLE STAKES
   Consumer expectation has shifted: no artificial colors, no undisclosed proprietary blends,
   and full ingredient transparency are now baseline expectations for D2C supplement buyers.
   Brands that can't show full ingredient disclosure on the label are losing customers to
   brands that can. NovaBotanics is well-positioned here — this is our core differentiator.
   Implication: Maintain and market our clean label standards aggressively.

2. STRESS & CORTISOL MANAGEMENT: FASTEST GROWING CATEGORY
   "Adaptogen" searches grew 340% YoY. Ashwagandha (especially KSM-66), rhodiola, and
   holy basil are the top ingredients. The driver: post-pandemic chronic stress awareness.
   The target demographic: 28-45 year olds, primarily women.
   Implication: Validates Q1 2026 ashwagandha launch. Timing is ideal.

3. SLEEP QUALITY OVER SLEEP SPEED
   Consumer language has shifted from "fall asleep faster" to "better sleep quality."
   This aligns with growing understanding that melatonin affects sleep onset but not
   sleep quality. L-theanine, glycine, and magnesium are growing in association with
   "sleep quality" searches. Implication: Our reformulated sleep gummies (L-theanine
   addition) are aligned with this trend. Lean into "sleep quality" language in marketing.

4. FUNCTIONAL MUSHROOMS: STRONG BUT NICHE
   Lion's Mane, Reishi, Chaga searches growing 180% YoY. Strong among biohacker/health
   optimization segment. However, quality claims are poorly regulated and consumer
   skepticism is growing about brands that can't prove extract standardization.
   Implication: Worth monitoring for Q3 2026 product consideration. Not a priority now.

5. PERSONALIZATION AS PREMIUM POSITIONING
   Subscription brands offering "personalized supplement stacks" command 20-30% price premium.
   Leading players: Gainful (protein), Persona (daily packs), Rootine (micronutrient testing).
   Implication: Bundle strategy is a step toward personalization. Consider quiz-based product
   recommendation flow on website as near-term initiative.

6. GLP-1/OZEMPIC ADJACENT MARKET
   Semaglutide users are a growing supplement buyer segment — they need protein, fiber,
   B12, and muscle support to offset GLP-1 medication side effects. Several D2C brands
   are explicitly targeting this segment. Implication: Not immediately relevant but worth
   tracking as segment grows.

7. SUBSCRIPTION MODEL DOMINANCE
   85% of D2C supplement revenue in 2025 came from subscription customers.
   Average subscription LTV is 4.7x one-time purchase LTV. Brands investing in subscription
   UX and retention are dramatically outperforming transactional models.
   Implication: Our subscription structure is critical. Bundle discount tiers (approved Nov 2025)
   directly address this trend.

8. SPORTS NUTRITION CROSSING INTO WELLNESS
   NSF Sport certification is increasingly sought by wellness (non-athlete) customers who
   view it as a general quality signal, not just an athlete requirement. Clean sport
   crossover is driving premium positioning.
   Implication: Our Greens Powder NSF certification should be more prominently marketed
   to wellness customers, not just athletes.

9. TRANSPARENCY AS BRAND MOAT
   Brands publishing COAs publicly, sharing third-party lab results, and disclosing sourcing
   are building higher customer trust and lower acquisition cost (organic word-of-mouth).
   Implication: Consider a public COA library on the website. Low cost, high trust signal.

10. SHORT-FORM VIDEO AS DOMINANT ACQUISITION CHANNEL
    TikTok Shop and Instagram Reels now drive 43% of new customer acquisition for D2C
    supplement brands. Science-based, ingredient-explainer content outperforms before/after
    content by 2.8x for supplement brands.
    Implication: Marketing to invest in ingredient spotlight video content. Align with
    brand voice (science-backed, approachable). Creator briefs must include no health claims.
"""
    write_txt(BASE_DIR / "competitor_intel" / "Market_Trends_Wellness_2026.txt", content)


def gen_competitor_listings():
    content = """COMPETITOR AMAZON PRODUCT LISTINGS - SCRAPED TEXT
NovaBotanics Competitive Intel | October 2025
================================================

LISTING 1: ZenLeaf Sleep Support Gummies
URL: amazon.com/dp/[competitor]
Price: $28.99 | Rating: 4.1/5 | Reviews: 3,847 | BSR: #12 in Sleep Aids
----------------------------------------
Title: ZenLeaf Sleep Support Gummies | Melatonin 5mg | Natural Sleep Aid | 60 Count

Bullet Points:
• FAST-ACTING SLEEP SUPPORT: Our melatonin gummies help you fall asleep faster and stay asleep longer for a full night of rest
• NATURAL INGREDIENTS: Made with melatonin 5mg and chamomile extract for a gentle, effective sleep formula
• GREAT TASTING: Available in Mixed Berry and Mango flavors — our gummies actually taste good
• NO HABIT FORMING: Safe for regular use, helps reset your sleep schedule naturally
• QUALITY ASSURED: Made in FDA-registered facility, third-party tested for purity

Description:
ZenLeaf Sleep Support Gummies help you get the rest you deserve. Our formula combines melatonin
with chamomile for a time-tested approach to better sleep. Available in Mixed Berry flavor.
Great for jet lag, shift workers, and anyone who has trouble falling asleep.

Price breakdown: $28.99/60ct = $0.48/serving
Notable: Mixed Berry flavor option; 5mg melatonin; no L-theanine; contains Red 40 (artificial color)

---

LISTING 2: MoonRest Premium Sleep Gummies
URL: amazon.com/dp/[competitor]
Price: $53.99 | Rating: 4.4/5 | Reviews: 1,203 | BSR: #34 in Sleep Aids
----------------------------------------
Title: MoonRest Premium Sleep Gummies | 10mg Melatonin + L-Theanine 200mg + Magnesium | 60ct

Bullet Points:
• PREMIUM TRIPLE-ACTION FORMULA: Melatonin for sleep onset, L-theanine for calm, magnesium for deep sleep
• HIGH-POTENCY MELATONIN: 10mg per serving for even the most challenging sleep situations
• MAXIMUM L-THEANINE: 200mg L-theanine promotes relaxation without sedation
• CLEAN-LABEL COMMITMENT: No artificial dyes, no high fructose corn syrup
• PHYSICIAN-FORMULATED: Developed with sleep medicine practitioners

Description:
The premium choice for serious sleep support. MoonRest's triple-action formula addresses
every stage of sleep: onset, depth, and quality. High-dose melatonin for fast results,
L-theanine for relaxed mental state, and magnesium for deep sleep stages.

Price breakdown: $53.99/60ct = $0.90/serving
Notable: Strong clean label positioning; 10mg melatonin is too high per clinical guidelines;
high L-theanine dose (200mg vs our 100mg); premium price anchors perception

---

LISTING 3: DreamWell Sleep Gummies
URL: amazon.com/dp/[competitor]
Price: $41.99 | Rating: 4.3/5 | Reviews: 892 | BSR: #28 in Sleep Aids
----------------------------------------
Title: DreamWell Advanced Sleep Gummies | Melatonin 5mg + GABA 100mg + L-Theanine 100mg | Vegan

Bullet Points:
• ADVANCED TRIPLE FORMULA: Melatonin, GABA, and L-Theanine work together for complete sleep support
• GABA SUPPORT: GABA helps quiet the mind and reduce the mental chatter that keeps you awake
• VEGAN & GLUTEN FREE: Made with plant-based pectin, no gelatin
• MODERN FORMULA: Beyond basic melatonin — a comprehensive sleep support stack
• 30-DAY GUARANTEE: Full refund if not satisfied

Description:
DreamWell takes sleep gummies to the next level. We don't just include melatonin — we've built
a comprehensive sleep support stack with GABA and L-theanine. Vegan-friendly pectin base.

Price breakdown: $41.99/60ct = $0.70/serving
Notable: GABA's efficacy in oral supplement form is limited (poor BBB crossing). 5mg melatonin
still high. Vegan positioning (pectin vs gelatin) is a differentiator we could match.
"""
    write_txt(BASE_DIR / "competitor_intel" / "Amazon_Competitor_Listings_Scraped.txt", content)


def gen_competitor_social():
    content = """COMPETITOR SOCIAL CONTENT AUDIT
NovaBotanics Internal Research | Q3-Q4 2025
================================================

METHODOLOGY
-----------
Analyzed Instagram and TikTok content for top 4 sleep supplement competitors over 90-day
period (July-September 2025). Tracked post types, engagement rates, and themes.

ZENLEAF SLEEP SUPPORT (@zenleafsleep)
--------------------------------------
Follower count: 41,200 (Instagram) | 28,900 (TikTok)
Posting frequency: 5x/week Instagram, 3x/week TikTok
Average engagement rate: 2.1% (below industry average of 3.4% for supplements)

Content breakdown:
  - 45% product glamour shots / lifestyle imagery
  - 25% customer testimonials (screenshot reposts)
  - 20% promotional content (discount codes, giveaways)
  - 10% educational content (what is melatonin, sleep hygiene tips)

Top performing content types (by engagement):
  1. Before/after sleep tracking screenshots from customers — avg 4.2% engagement
  2. "3 signs you have poor sleep quality" educational posts — avg 3.8% engagement
  3. Giveaway posts — avg 6.1% engagement but low comment quality (mostly entries)

Weaknesses:
  - Almost no ingredient education or science content
  - Customer testimonials are generic ("I sleep so well now!") — no specifics
  - Promotional content frequency is high — trains audience to wait for discounts
  - Comments with "makes me groggy" go unresponded

Key takeaway: ZenLeaf wins on volume/reach but not on trust or education.

---

MOONREST PREMIUM (@moonrestsleep)
----------------------------------
Follower count: 18,700 (Instagram) | 31,400 (TikTok)
Posting frequency: 3x/week Instagram, 5x/week TikTok
Average engagement rate: 4.8% (above average — TikTok-led strategy)

Content breakdown:
  - 40% ingredient education (L-theanine explainers, magnesium science)
  - 30% lifestyle / aesthetic content (sophisticated, premium feel)
  - 20% customer results (Oura ring data, testimonials)
  - 10% behind-the-scenes (founder content)

Top performing content types:
  1. "Why 10mg melatonin is actually bad for you" — controversial hook, 8.2% engagement
  2. Oura ring / sleep tracker data from customers — 6.7% engagement
  3. Founder explaining formulation decisions — 5.9% engagement

Key takeaway: MoonRest's science content performs well. Interesting that they position
against high-dose melatonin while themselves using 10mg — customer comments point this out.

---

DREAMWELL (@dreamwellsleep)
-----------------------------
Follower count: 12,400 (Instagram) | 22,100 (TikTok)
Posting frequency: 4x/week Instagram, 4x/week TikTok
Average engagement rate: 3.2%

Content breakdown:
  - 50% trendy/aesthetic content (purple color palette, moon imagery)
  - 30% promotional
  - 20% educational (mostly GABA content — despite limited evidence)

Top performing: Aesthetic product shots with purple mood lighting (strong visual brand).
Weakness: Leans heavily on GABA as differentiator but scientific support for oral GABA
is weak. Several TikTok comments point this out. Brand hasn't responded well.

---

WHAT CONTENT WORKS ACROSS ALL COMPETITORS
-------------------------------------------
Based on cross-competitor analysis, highest engagement content types are:

1. INGREDIENT SCIENCE EXPLAINERS (3.5-8% engagement)
   "What does L-theanine actually do?" style content. Audience is increasingly sophisticated
   and wants to understand the why behind ingredients. Short (60-90 second) video performs best.

2. SLEEP TRACKER DATA (4-7% engagement)
   Actual sleep data (Oura, Apple Watch, Whoop) from real customers showing changes after
   using the product. Authentic, specific, and quantified. More compelling than generic testimonials.

3. FORMULATION TRANSPARENCY (4-6% engagement)
   Founder/brand explaining WHY they chose specific ingredients and doses. Performs especially
   well when it positions against industry norms ("why we use 3mg not 10mg melatonin").

4. "MYTHS ABOUT SLEEP SUPPLEMENTS" STYLE CONTENT (3-5% engagement)
   Educational content that addresses common misconceptions. Positions brand as trustworthy
   authority. Drives saves more than likes (good for algorithm).

CONTENT GAP OPPORTUNITIES FOR NOVABOTANICS
---------------------------------------------
1. No competitor is doing deep-dive L-theanine content despite it being the most
   differentiating ingredient. We could own this topic.
2. "Why we reduced our melatonin dose" is a compelling reformulation story no one has told.
3. Clean label content: no competitor is doing systematic "here's exactly what's in our product
   and why we chose each ingredient" series. This aligns perfectly with our brand voice.
4. Subscription value content: no competitor is showing the "cost per good night of sleep"
   math. At $0.48/serving on subscription, that's a compelling number.
"""
    write_txt(BASE_DIR / "competitor_intel" / "Competitor_Social_Content_Audit.txt", content)


# ─────────────────────────────────────────────
# WORKSPACE 4: SUPPLIER INTEL
# ─────────────────────────────────────────────

def gen_coa():
    content = """CERTIFICATE OF ANALYSIS
Product: Ashwagandha Root Extract (KSM-66)
Supplier: PurePlant Ingredients (Supplier A)
Lot Number: PP-ASH-KSM-2510
Manufacturing Date: October 15, 2025
Expiration Date: October 14, 2027
Country of Origin: India
================================================

PRODUCT IDENTIFICATION
----------------------
INCI Name: Withania somnifera root extract
Common Name: Ashwagandha KSM-66
Standardization: Minimum 5% withanolides by HPLC
Form: Fine brown powder
Appearance: Light brownish-beige free-flowing powder
Odor: Characteristic earthy/herbal
Taste: Slightly bitter, characteristic

IDENTITY TESTING
----------------
Test: Botanical Identity (macroscopic)
Method: Visual inspection vs reference standard
Result: PASS — consistent with Withania somnifera root

Test: TLC Fingerprint
Method: TLC vs authenticated reference
Result: PASS — matches reference chromatographic profile

Test: HPLC Withanolide Quantification
Method: HPLC-UV
Specification: NLT 5.0% withanolides
Result: 5.8% withanolides
Status: PASS

HEAVY METALS TESTING
--------------------
(All results in ppm unless noted)

Lead (Pb)
  Specification: NMT 1.0 ppm
  Result: 0.08 ppm
  Status: PASS

Cadmium (Cd)
  Specification: NMT 0.3 ppm
  Result: 0.02 ppm
  Status: PASS

Mercury (Hg)
  Specification: NMT 0.1 ppm
  Result: <0.01 ppm (below detection limit)
  Status: PASS

Arsenic (As)
  Specification: NMT 1.5 ppm
  Result: 0.11 ppm
  Status: PASS

MICROBIOLOGICAL TESTING
------------------------
Total Aerobic Plate Count
  Specification: NMT 10,000 CFU/g
  Result: 280 CFU/g
  Status: PASS

Total Yeast and Mold Count
  Specification: NMT 1,000 CFU/g
  Result: 45 CFU/g
  Status: PASS

E. coli
  Specification: Absent in 1g
  Result: Absent
  Status: PASS

Salmonella spp.
  Specification: Absent in 25g
  Result: Absent
  Status: PASS

Staphylococcus aureus
  Specification: Absent in 1g
  Result: Absent
  Status: PASS

PESTICIDE RESIDUE SCREENING
-----------------------------
Method: LC-MS/MS multi-residue screen (400+ compounds)
Result: No detectable pesticide residues above LOQ
Status: PASS

SOLVENT RESIDUE TESTING
------------------------
Method: Headspace GC-FID/MS
Result: No Class 1 or Class 2 solvents detected
Status: PASS

PHYSICAL & CHEMICAL
--------------------
Moisture Content
  Specification: NMT 5.0%
  Result: 3.2%
  Status: PASS

Particle Size (80% through 60 mesh)
  Specification: NLT 80%
  Result: 94%
  Status: PASS

Bulk Density: 0.42 g/mL

CONCLUSION
----------
This lot (PP-ASH-KSM-2510) meets all established specifications for purity, identity,
potency, and safety. Approved for use in dietary supplement manufacturing.

Certified by: Dr. Anika Sharma, Quality Director, PurePlant Ingredients
Date of Certification: November 1, 2025
Laboratory: IndoAnalytical Labs (ISO/IEC 17025 accredited)

Third-Party Verification: This COA is supported by independent testing at IndoAnalytical Labs.
Certificate available upon request. Lab accreditation: NABL/ISO 17025 #TC-5291.
"""
    write_txt(BASE_DIR / "supplier_intel" / "COA_KSM66_Ashwagandha_SupplierA.txt", content)


def gen_supplier_pricing():
    rows = [
        ("PurePlant (Supplier A)", "Ashwagandha KSM-66", "$285", "5kg", "45", "India", "KSM-66 licensed, ISO 9001, FSSC 22000"),
        ("GreenSource (Supplier B)", "Ashwagandha KSM-66", "$328", "3kg", "21", "India", "KSM-66 licensed, ISO 9001"),
        ("PurePlant (Supplier A)", "L-Theanine (Suntheanine)", "$420", "5kg", "45", "Japan", "Suntheanine licensed, GRAS"),
        ("GreenSource (Supplier B)", "L-Theanine (generic)", "$195", "10kg", "28", "China", "ISO 9001"),
        ("PurePlant (Supplier A)", "Melatonin USP Grade", "$1,250", "1kg", "45", "USA", "USP grade, cGMP"),
        ("GreenSource (Supplier B)", "Melatonin USP Grade", "$1,480", "500g", "21", "USA", "USP grade, cGMP"),
        ("BotanicalPrime (Supplier C)", "Turmeric Extract 95% curcuminoids", "$145", "10kg", "30", "India", "ISO 9001, organic certified"),
        ("PurePlant (Supplier A)", "Turmeric Extract 95% curcuminoids", "$165", "5kg", "45", "India", "ISO 9001, FSSC 22000"),
        ("BotanicalPrime (Supplier C)", "BioPerine (black pepper extract)", "$580", "5kg", "30", "India", "Sabinsa licensed"),
        ("GreenSource (Supplier B)", "Magnesium Glycinate Bisglycinate", "$195", "10kg", "21", "USA", "Albion chelated, GRAS"),
        ("PurePlant (Supplier A)", "Magnesium Glycinate Bisglycinate", "$210", "5kg", "45", "USA", "Albion chelated, GRAS, FSSC 22000"),
        ("BotanicalPrime (Supplier C)", "Spirulina Organic", "$88", "25kg", "35", "USA", "USDA Organic, Non-GMO"),
        ("PurePlant (Supplier A)", "Chlorella Organic", "$112", "10kg", "45", "Japan", "USDA Organic, Informed Sport"),
    ]
    write_csv(
        BASE_DIR / "supplier_intel" / "Supplier_Pricing_Comparison_2026.csv",
        ["supplier", "ingredient", "price_per_kg", "moq", "lead_time_days", "origin_country", "certifications"],
        rows
    )


def gen_supplier_correspondence():
    content = """SUPPLIER CORRESPONDENCE ARCHIVE
NovaBotanics Procurement | Q3-Q4 2025
Compiled by: Sam (Operations)
================================================

THREAD 1: PurePlant (Supplier A) — Ashwagandha KSM-66 Negotiation
------------------------------------------------------------------

FROM: Sam Okafor <sam@novabotanics.com>
TO: Raj Mehta <r.mehta@pureplant.com>
DATE: September 15, 2025
SUBJECT: Q4 2025 Ashwagandha KSM-66 Order Quote

Hi Raj,

We're forecasting a Q1 2026 product launch featuring KSM-66 ashwagandha and wanted to
start the conversation early on pricing and lead times.

Anticipated Q4 order: 20kg (pilot + buffer stock)
Anticipated ongoing monthly volume once launched: 8-12kg/month

Can you confirm:
1. Current price per kg at 20kg MOQ
2. Lead time from order to our warehouse
3. Availability of your latest COA

Looking forward to working with you on this one.

Best,
Sam

---

FROM: Raj Mehta <r.mehta@pureplant.com>
TO: Sam Okafor <sam@novabotanics.com>
DATE: September 17, 2025
SUBJECT: RE: Q4 2025 Ashwagandha KSM-66 Order Quote

Hi Sam,

Great timing — we just restocked KSM-66 from our October harvest lot.

Pricing:
  5kg MOQ: $295/kg
  10kg+: $285/kg
  20kg+: $272/kg (I can offer this given your volume commitment)

Lead time: 45 days from confirmed PO to your warehouse (customs + domestic freight).
We can expedite to 32 days with air freight at +$185 flat fee.

COA attached. Lot PP-ASH-KSM-2510, certified November 1, 2025.
Withanolide content: 5.8% (spec is NLT 5.0%). Heavy metals all clean.

Note: Our next production run is January 2026. If you anticipate needing more than 20kg
in Q1, I'd recommend placing a blanket order now to lock pricing and availability.

Best,
Raj

---

FROM: Sam Okafor <sam@novabotanics.com>
TO: Raj Mehta <r.mehta@pureplant.com>
DATE: September 22, 2025
SUBJECT: RE: Q4 2025 Ashwagandha KSM-66 Order Quote

Raj,

Thanks for the quick turnaround. COA looks excellent — 5.8% withanolides is above spec
which we like.

Two questions before we move forward:
1. Can you hold 20kg at the $272/kg rate while we finalize internal approval? Est. 2 weeks.
2. Is Suntheanine (L-theanine) also available from you? We have an ongoing need.

If you can confirm hold and L-theanine availability, I'll have a PO for both ready by Oct 10.

Sam

---

FROM: Raj Mehta <r.mehta@pureplant.com>
TO: Sam Okafor <sam@novabotanics.com>
DATE: September 23, 2025
SUBJECT: RE: Q4 2025 Ashwagandha KSM-66 Order Quote

Sam,

Happy to hold the 20kg at $272/kg through October 8.

On Suntheanine: Yes, we carry it. Current pricing $420/kg at 5kg MOQ. Lead time same 45
days (sourced from Japan, licensed from Taiyo International). COA available on request.

Confirmed we can combine the shipment for both — saves you the per-order freight cost.

Best,
Raj

---
---

THREAD 2: GreenSource (Supplier B) — Delivery Delay Resolution
--------------------------------------------------------------

FROM: Sam Okafor <sam@novabotanics.com>
TO: Lisa Chen <l.chen@greensource.co>
DATE: October 3, 2025
SUBJECT: PO #GS-2025-0882 — Delivery Status

Hi Lisa,

Following up on PO #GS-2025-0882 (Magnesium Glycinate, 10kg). Ship date was Sept 28 per
our agreement. We're now 5 days past ship date with no tracking update.

Our production run is scheduled for October 20. If this doesn't arrive by October 15 we'll
have a serious disruption.

Can you provide an updated ETA and tracking information today?

Sam

---

FROM: Lisa Chen <l.chen@greensource.co>
TO: Sam Okafor <sam@novabotanics.com>
DATE: October 3, 2025
SUBJECT: RE: PO #GS-2025-0882 — Delivery Status

Hi Sam,

I sincerely apologize for the delay. There was a carrier issue at our outbound facility —
a dock strike (now resolved) delayed all outbound shipments 6-7 business days.

Your order shipped this morning. Tracking: UPS 1Z849W980310676285
Expected delivery: October 10, 2025.

That gives you 10 days before your production run. We'll expedite at our cost if anything
further delays.

Again, I'm sorry for the disruption. I'll flag your account for priority handling going forward.

Lisa

---

FROM: Sam Okafor <sam@novabotanics.com>
TO: Lisa Chen <l.chen@greensource.co>
DATE: October 10, 2025
SUBJECT: RE: PO #GS-2025-0882 — Received

Lisa,

Order received today. Packaging looks intact. QC check passed.

Given this delay, I want to discuss whether GreenSource can commit to a guaranteed lead
time with a penalty clause going forward. We're building more products and need reliable
logistics. If you can offer a 21-day guaranteed lead time (vs current "estimated"), that
would help us prioritize GreenSource for more SKUs.

Can we get on a call this week?

Sam

---

FROM: Lisa Chen <l.chen@greensource.co>
TO: Sam Okafor <sam@novabotanics.com>
DATE: October 11, 2025
SUBJECT: RE: PO #GS-2025-0882 — Received

Sam,

Glad it arrived safely. Yes — a call makes sense.

I can commit to a 21-day guaranteed lead time for all US-sourced ingredients (magnesium,
some botanicals). For internationally-sourced items (KSM-66, L-theanine), 28 days is more
realistic with a guarantee.

I'll also offer a 5% discount on the next 3 orders to acknowledge this disruption.

Available Monday or Tuesday this week. What works for you?

Lisa

---
---

THREAD 3: BotanicalPrime (Supplier C) — Quality Concern
--------------------------------------------------------

FROM: Sam Okafor <sam@novabotanics.com>
TO: David Torres <d.torres@botanicalprime.com>
DATE: October 18, 2025
SUBJECT: Turmeric Extract Lot BP-TUR-2509 — Curcuminoid Content Question

David,

We received Lot BP-TUR-2509 (Turmeric Extract 95% curcuminoids, 10kg) last week.

Our internal QC team is running their standard HPLC test and getting 91.3% curcuminoids,
not the 95% stated in your COA. That's a significant gap and puts this lot below spec for
our formulation.

Can you:
1. Share your raw HPLC data for this lot
2. Confirm the testing lab and method used
3. Advise on what happens if our test and your COA don't reconcile

We have a production run in 2 weeks and need resolution quickly.

Sam

---

FROM: David Torres <d.torres@botanicalprime.com>
TO: Sam Okafor <sam@novabotanics.com>
DATE: October 19, 2025
SUBJECT: RE: Turmeric Extract Lot BP-TUR-2509 — Curcuminoid Content Question

Sam,

Thank you for flagging this. I've pulled the QC records for lot BP-TUR-2509.

Our HPLC test (conducted at IndoTest Labs, Oct 5, 2025) showed 94.7% curcuminoids,
which we rounded to 95% per spec as it's within rounding tolerance.

However, a 3.4% gap between your result and ours is outside normal analytical variation.
The most likely explanations are:
  a) Different HPLC method (our method is AOAC 2012.04; different methods can yield
     different curcuminoid measurements)
  b) Sample preparation variation
  c) The lot is at the lower bound of spec

I'd like to:
  1. Send you our raw chromatogram data
  2. Arrange for a split-sample re-test at a mutually agreed laboratory

If the independent test confirms your result (below 95%), we will replace the lot at
no charge and cover your shipping.

I'm sorry for the disruption. This is not the standard we hold ourselves to.

David

---

FROM: Sam Okafor <sam@novabotanics.com>
TO: David Torres <d.torres@botanicalprime.com>
DATE: October 20, 2025
SUBJECT: RE: Turmeric Extract Lot BP-TUR-2509 — Resolution

David,

Thank you for the prompt and professional response. Split-sample test at IndoAnalytical Labs
(our preferred third-party) is agreed. We'll send samples by October 22.

Please send the chromatogram data in the meantime.

If the result confirms our reading, we'll need the replacement lot by November 1 to stay
on production schedule. Please confirm you can commit to that timeline if replacement is needed.

Sam

[Update note added November 5, 2025: Independent test confirmed 91.8% curcuminoids.
BotanicalPrime shipped replacement lot at no charge. Replacement received November 4 with
COA showing 95.4% curcuminoids. Issue resolved. Added quality note to BotanicalPrime vendor
record: conduct independent HPLC verification on first lot of each new ingredient.]
"""
    write_txt(BASE_DIR / "supplier_intel" / "Supplier_Correspondence_Archive.txt", content)


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────

def main():
    print("Setting up directories...")
    setup_dirs()

    print("\nGenerating Customer Voice files...")
    gen_amazon_reviews()
    gen_shopify_reviews()
    gen_support_tickets()
    gen_social_mentions()

    print("\nGenerating Team Brain files...")
    gen_brand_guidelines()
    gen_sop_launch()
    gen_meeting_notes()
    gen_onboarding()
    gen_pricing_strategy()

    print("\nGenerating Competitor Intel files...")
    gen_competitor_analysis()
    gen_market_trends()
    gen_competitor_listings()
    gen_competitor_social()

    print("\nGenerating Supplier Intel files...")
    gen_coa()
    gen_supplier_pricing()
    gen_supplier_correspondence()

    print("\nDone. All files written to:", BASE_DIR.resolve())
    print("\nFile summary:")
    for ws in WORKSPACES:
        files = list((BASE_DIR / ws).glob("*"))
        print(f"  {ws}/: {len(files)} files")


if __name__ == "__main__":
    main()
