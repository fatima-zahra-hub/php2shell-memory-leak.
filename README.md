# PHP2Shell Memory Exhaustion (OOM) Simulation
This is a vulnerable Flask app simulating a memory exhaustion bug that leads to data leakage upon crashing.

## How to run
1. `pip install flask`
2. `python app.py`
3. Send multiple POST requests with files to `/upload` to trigger OOM.
