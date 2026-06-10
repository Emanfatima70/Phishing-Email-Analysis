# Simple Phishing Email Analyzer (SOC Level Beginner Tool)

email = open("Samples/email1.txt", "r").read()

print("=== EMAIL ANALYSIS REPORT ===\n")

# Check sender
if "paypal" in email or "security" in email:
    print("[!] Suspicious sender detected")

# Check urgency keywords
if "urgent" in email.lower():
    print("[!] Urgent language detected (possible phishing)")

# Check fake links
if "http://" in email:
    print("[!] Insecure link found")

print("\n=== ANALYSIS COMPLETE ===")# Email Header Analyzer 
