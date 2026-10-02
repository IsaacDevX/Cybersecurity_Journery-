failed_attempts = 7
max_allowed = 5

if failed_attempts > max_allowed:
    print("⚠️ ALERT: Brute-force attack detected on IP 192.168.1.100")
    risk_score = failed_attempts * 1.5
    print("Risk Score:", risk_score)
else:
    print("✅ Login attempts within normal range")
