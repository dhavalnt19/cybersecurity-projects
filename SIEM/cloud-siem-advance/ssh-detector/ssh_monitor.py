from collections import defaultdict
from alerting.email_alert import send_alert

LOG_FILE = "../logs/sample_auth.log"
THRESHOLD = 5

failed_attempts = defaultdict(int)

with open(LOG_FILE, "r") as f:
    for line in f:
        if "Failed password" in line:
            ip = line.split()[-1]
            failed_attempts[ip] += 1

for ip, count in failed_attempts.items():
    if count > THRESHOLD:
        alert_msg = f"🚨 Brute force detected from {ip} ({count} attempts)"
        print(alert_msg)

        send_alert(
            subject="🚨 SSH Brute Force Alert",
            message=alert_msg
        )
