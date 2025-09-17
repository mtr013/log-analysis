# Log Analysis — Synthetic Log Generator

This small project generates synthetic host logs in JSON Lines format to help test analysis tools and notebooks.

Original analysis was done on a private dataset provided as a task by Yandex and excluded for privacy concerns.

The output is a JSON Lines file where each line is a JSON object with fields: host, uid, username, ip, timestamp (ISO8601Z), pid, ppid, process_name.

Files

- `generate_logs.py` — generator script
- `synthetic_logs.json` — generated logs (similar to original dataset)
- `log_analysis.ipynb` — notebook with log analysis