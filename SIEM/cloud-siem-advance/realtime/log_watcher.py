import time

LOG_FILE = "../logs/sample_auth.log"

def follow(file):
    file.seek(0, 2)
    while True:
        line = file.readline()
        if not line:
            time.sleep(0.5)
            continue
        yield line

def monitor():
    with open(LOG_FILE, "r") as f:
        loglines = follow(f)
        for line in loglines:
            if "Failed password" in line:
                print(f"🚨 REAL-TIME ALERT: {line.strip()}")

if __name__ == "__main__":
    monitor()
