import random
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

hosts = ["alpha.net", "beta.cloud", "gamma.org", "delta.io", "epsilon.local", 
         "zeta.org", "theta.net", "iota.cloud"]
users = ["alice", "bob", "charlie", "dave", "eve", "trent", "mallory", 
         "peggy", "root", "sysservice", "john", "lisa", "mike", "nancy"]
suspicious_users = ["root", "trent", "eve"]
dominant_ip = "10.99.99.99"
ips = ["10.0.{}.{}".format(i, j) for i in range(1, 50) for j in range(1, 50)]
processes = ["ssh", "scp", "rsync", "python3", "vim", "ping", "curl", "ftp", "sshfs"]

start_date = datetime(2025, 8, 1)
num_days = 15
normal_events = 500
low_events = 200
high_events = 800

low_anomalies = [3]
high_anomalies = [7]

def random_timestamp(day_index):
    base = start_date + timedelta(days=day_index)
    delta = timedelta(seconds=random.randint(0, 86399))
    return (base + delta).isoformat() + "Z"

def generate_event(user, host, day_index, ip=None, pid_ppid=None):
    pid, ppid = pid_ppid if pid_ppid else (random.randint(1000, 9999), random.randint(1000, 9999))
    return {
        "host": host,
        "uid": random.randint(100, 9999),
        "username": user,
        "ip": ip if ip else random.choice(ips),
        "timestamp": random_timestamp(day_index),
        "pid": pid,
        "ppid": ppid,
        "process_name": random.choice(processes)
    }

log_events = []

for day_index in range(num_days):
    if day_index in low_anomalies:
        num_events = low_events
    elif day_index in high_anomalies:
        num_events = high_events
    else:
        num_events = normal_events

    # Ensure suspicious users are present
    base_sus = len(suspicious_users) * 5
    for _ in range(base_sus):
        host = random.choice(hosts)
        user = random.choice(suspicious_users)
        ip = dominant_ip if random.random() < 0.7 else None
        log_events.append(generate_event(user, host, day_index, ip=ip))

    for _ in range(num_events - base_sus):
        host = random.choice(hosts)
        if day_index in high_anomalies and random.random() < 0.4:
            user = random.choice(suspicious_users)
        else:
            user = random.choice(users)
        ip = dominant_ip if user in suspicious_users and random.random() < 0.5 else None
        log_events.append(generate_event(user, host, day_index, ip=ip))

chain_hosts = random.sample(hosts, 3)
pid_base = 5000
for host in chain_hosts:
    for i in range(3):  # 3 chains per host
        start_pid = pid_base + i*10
        for j in range(5):  # chain length 5
            log_events.append(generate_event(
                random.choice(suspicious_users),
                host,
                random.randint(0, num_days-1),
                pid_ppid=(start_pid+j, start_pid+j-1 if j>0 else 0)
            ))

df = pd.DataFrame(log_events)
df.to_json("synthetic_logs.json", orient="records", lines=True)