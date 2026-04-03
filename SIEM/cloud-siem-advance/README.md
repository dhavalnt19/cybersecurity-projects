🔐 Advanced Cloud SIEM & Threat Detection Lab










📌 Overview

This project simulates a real-world SIEM (Security Information and Event Management) system using Python and cloud concepts.

It detects and responds to:

🚨 SSH brute force attacks
📁 Unauthorized file changes
🦠 Malware using hash detection

Includes real-time monitoring and automated alerting, similar to SOC environments.

🚀 Features
Real-time log monitoring
SSH brute force detection
File Integrity Monitoring (FIM)
Malware hash detection
Email alert system
MITRE ATT&CK mapping
Modular architecture
🏗️ Project Structure

cloud-siem-advanced/
├── fim/
├── ssh-detector/
├── malware-scanner/
├── alerting/
├── realtime/
├── logs/
├── mitre/
├── aws/
└── README.md

⚙️ Setup Instructions
1. Clone Repository

git clone https://github.com/yourusername/cloud-siem-advanced.git

cd cloud-siem-advanced

2. Setup Email Alerts (Mac/Linux)

export EMAIL_USER="your_email@gmail.com
"
export EMAIL_PASS="your_app_password"
export EMAIL_TO="your_email@gmail.com
"

3. Prepare Logs

mkdir -p logs
touch logs/sample_auth.log

🧪 TESTING & OUTPUTS
🔥 SSH Brute Force Detection

Simulate attack:

echo "Failed password for root from 192.168.1.100 port 22 ssh2" >> logs/sample_auth.log

(Repeat 6+ times)

Run:

python3 ssh-detector/ssh_monitor.py

Output:

🚨 Brute force detected from 192.168.1.100 (6 attempts)
📧 Alert email sent successfully!

MITRE: T1110 (Brute Force)

🔥 Real-Time Monitoring

Run:

python3 realtime/log_watcher.py

Simulate:

echo "Failed password for root from 192.168.1.200 port 22 ssh2" >> logs/sample_auth.log

Output:

🚨 REAL-TIME ALERT: Failed password for root from 192.168.1.200

🔥 File Integrity Monitoring (FIM)

echo "hello" > test.txt
python3 fim/fim.py

echo "hacked" > test.txt
python3 fim/fim.py

Output:

🚨 ALERT: test.txt modified!

MITRE: T1565.001

🔥 Malware Hash Detection

python3 malware-scanner/hash_scan.py

Output:

✅ File clean

MITRE: T1204

📧 Email Alert Example

Subject: 🚨 SSH Brute Force Alert

Message:
Brute force detected from 192.168.1.100 (6 attempts)

☁️ AWS Integration
EC2 → Log source
CloudWatch → Log monitoring
SNS → Alerts
IAM → Secure access

See aws/setup.md

🧠 MITRE ATT&CK Summary

SSH Detection → T1110
FIM → T1565.001
Malware → T1204

🔐 Security Best Practices
Environment variables for credentials
Modular design
Real-time detection
Automated alerts
🎯 Learning Outcomes
Built SIEM-like system
Implemented threat detection
Used MITRE ATT&CK
Created alerting system
📸 Screenshots

(Add screenshots here)

👨‍💻 Author

Dhaval Talekar

🚀 Future Improvements
AWS Lambda auto-response
IP blocking
Threat intelligence API
Dashboard (Kibana/Grafana)

💬 Explanation

“I built a real-time SIEM system that detects brute-force attacks, monitors file integrity, maps threats to MITRE ATT&CK, and sends automated alerts using Python and AWS.”
