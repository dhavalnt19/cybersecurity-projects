import re
from collections import defaultdict

LOG_FILE = "auth.log"   # use your sample log
THRESHOLD = 5

ip_attempts = defaultdict(int)
ip_logs = defaultdict(list)

with open(LOG_FILE, "r") as f:
    for line in f:
        if "Failed password" in line:
            match = re.search(r"from (\d+\.\d+\.\d+\.\d+)", line)
            if match:
                ip = match.group(1)
                ip_attempts[ip] += 1
                ip_logs[ip].append(line.strip())

# Output
for ip, count in ip_attempts.items():
    if count >= THRESHOLD:
        print("\n" + "="*50)
        print(f"🚨 Brute Force Detected!")
        print(f"IP Address: {ip}")
        print(f"Attempts: {count}")
        print("-"*50)
        print("📜 Logs:")
        
        for log in ip_logs[ip]:
            print(log)

        print("="*50)

