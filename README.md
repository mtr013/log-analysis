# Log Analysis | Synthetic Log Generator

This small project generates synthetic host logs in JSON Lines format to help test analysis tools and notebooks.

The original analysis used a private dataset and is excluded from this repository for privacy reasons. The synthetic logs here are generated to resemble statistical properties of the original data while avoiding any real user or host identifiers.

The generator writes a JSON Lines file where each line is a JSON object with the following fields:

- `host`: hostname where the event occurred
- `uid`: numeric user id
- `username`: account name
- `ip`: source IP address
- `timestamp`: ISO8601 timestamp (UTC)
- `pid`, `ppid`: process id and parent process id (may be null)
- `process_name`: name of the process

Files

- `generate_logs.py`: generator script
- `synthetic_logs.json`: sample output produced by the generator
- `log_analysis.ipynb`: notebook showing common analyses (events/day, top IPs, suspicious users, process chains)
