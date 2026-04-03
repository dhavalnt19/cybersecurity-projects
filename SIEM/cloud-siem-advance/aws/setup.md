# AWS Setup Guide

## 1. Launch EC2 Instance
- Amazon Linux / Ubuntu
- Enable SSH (port 22)

## 2. Install Python
sudo apt update
sudo apt install python3 -y

## 3. Clone Repo
git clone https://github.com/yourusername/cloud-siem-advanced.git

## 4. Run Scripts
cd realtime
python3 log_watcher.py

## 5. Enable CloudWatch Logs
- Install CloudWatch agent
- Send /var/log/auth.log

## 6. SNS Alerts
- Create SNS topic
- Subscribe email
- Trigger alerts via Lambda (optional)

## 7. IAM Role
- Attach CloudWatchFullAccess
