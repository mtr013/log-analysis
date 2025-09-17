import random
import json
from datetime import datetime, timedelta

# Config
num_logs = 200  # total log entries
start_date = datetime(2025, 8, 1)
end_date = datetime(2025, 8, 5)
hosts = ["alpha.net", "beta.cloud", "gamma.org", "delta.io", "epsilon.local"]
usernames = ["alice", "bob", "charlie", "dave", "eve", "mallory", "trent", "peggy"]
processes = ["ssh", "scp", "ftp", "python3", "vim", "ping", "rsync", "curl"]

# Helper functions
def random_ip():
    return ".".join(str(random.randint(1, 254)) for _ in range(4))

def random_timestamp(start, end):
    delta = end - start
    random_seconds = random.randint(0, int(delta.total_seconds()))
    return (start + timedelta(seconds=random_seconds)).strftime("%Y-%m-%dT%H:%M:%SZ")

# Generate logs
logs = []

for _ in range(num_logs):
    log = {
        "host": random.choice(hosts),
        "uid": random.randint(0, 9999),
        "username": random.choice(usernames),
        "ip": random_ip(),
        "timestamp": random_timestamp(start_date, end_date)
    }
    # 30% chance to include a process chain
    if random.random() < 0.3:
        log["pid"] = random.randint(1000, 9999)
        log["ppid"] = random.randint(1000, 9999)
        log["process_name"] = random.choice(processes)
    logs.append(log)

# Save to JSON file
with open("fake_logs.json", "w") as f:
    for entry in logs:
        f.write(json.dumps(entry) + "\n")

print(f"Generated {len(logs)} logs in 'fake_logs.json'")
