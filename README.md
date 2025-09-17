# Synthetic Log Generator & Analysis

## Description
This project generates synthetic host/system logs in JSON Lines format to help test analysis workflows and notebooks.  
The data is fully simulated, avoiding any real user or host information, while mimicking realistic patterns.

> **Note:** The original analysis used a private dataset and is excluded from this repository. The synthetic logs are generated to resemble statistical properties of the original data without exposing any real user or host identifiers.

## Key Features

- Generates events across multiple hosts and users
- Includes anomalous traffic spikes or dips
- Flags suspicious behaviours via high activity, multiple IPs, or unusual process activity
- Simulates process chains using PID–PPID relationships
- Fully compatible with log analysis pipelines and anomaly detection experiments

## Log Format

Each line in the JSON Lines file represents a single event with the following fields:

- `host` – hostname where the event occurred  
- `uid` – numeric user ID  
- `username` – account name  
- `ip` – source IP address  
- `timestamp` – ISO8601 timestamp (UTC)  
- `pid`, `ppid` – process ID and parent process ID (may be null)  
- `process_name` – name of the process  

## Files Included

- `generate_logs.py` – Python script to generate logs  
- `synthetic_logs.json` – Sample output produced by the generator  
- `log_analysis.ipynb` – Notebook demonstrating common analyses:
  - Events per day
  - Top IPs
  - Suspicious users
  - Process chains
