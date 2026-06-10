# SOC Multi-Email Phishing Analyzer

import os

folder = "Samples"

files = os.listdir(folder)

print("=== SOC EMAIL ANALYSIS DASHBOARD ===\n")

total_score = 0

for file in files:
    path = f"{folder}/{file}"
    email = open(path, "r", encoding="utf-8").read().lower()

    print(f"\nAnalyzing: {file}")
    score = 0

    if "paypal" in email or "netflix" in email:
        print("[HIGH RISK] Fake brand impersonation")
        score += 40

    if "urgent" in email or "immediately" in email:
        print("[MEDIUM RISK] Urgency detected")
        score += 20

    if "http://" in email:
        print("[HIGH RISK] Suspicious link detected")
        score += 30

    keywords = ["verify", "password", "login", "account", "suspend"]
    for k in keywords:
        if k in email:
            print(f"[INFO] Keyword found: {k}")
            score += 5

    print("Score:", score)
    total_score += score

print("\n======================")
print("TOTAL SOC SCORE:", total_score)

if total_score >= 120:
    print("RESULT: 🚨 MULTIPLE HIGH RISK PHISHING EMAILS")
elif total_score >= 60:
    print("RESULT: ⚠️ SUSPICIOUS ACTIVITY DETECTED")
else:
    print("RESULT: ✅ LOW RISK")