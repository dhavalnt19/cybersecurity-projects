import hashlib
import os
import json

BASELINE_FILE = "baseline.json"
TARGET_FILES = ["test.txt"]   # change this

def get_hash(file_path):
    with open(file_path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

def create_baseline():
    baseline = {}
    for file in TARGET_FILES:
        if os.path.exists(file):
            baseline[file] = get_hash(file)
    with open(BASELINE_FILE, "w") as f:
        json.dump(baseline, f)
    print("✅ Baseline created")

def check_integrity():
    with open(BASELINE_FILE, "r") as f:
        baseline = json.load(f)

    for file in TARGET_FILES:
        if os.path.exists(file):
            current_hash = get_hash(file)
            if baseline[file] != current_hash:
                print(f"🚨 ALERT: {file} modified!")
            else:
                print(f"✅ {file} is safe")

if not os.path.exists(BASELINE_FILE):
    create_baseline()
else:
    check_integrity()
