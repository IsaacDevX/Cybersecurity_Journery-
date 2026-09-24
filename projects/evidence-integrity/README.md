# Digital Evidence Integrity System

**Track:** H – Proving Digital Evidence Has Not Been Changed

## What It Does
A Python command-line tool that creates a SHA-256 hash of any digital file (evidence), stores it in a tamper-evident chain using SQLite, and verifies later that the file hasn't been altered.

## How It Works
1. **Collect** – Hash the file + record collector name, timestamp.
2. **Hash Chain** – Each new entry links to the previous one.
3. **Verify** – Re-hash the file and compare. Shows INTACT or TAMPERED.
4. **Report** – Generates a plain-English report for judges.
5. **Tamper Demo** – Simulates a tampering attack to prove detection works.

## Files
- `evidence.py` – Main CLI tool
- `tamper_demo.py` – Simulates tampering
- `demo.sh` – Runs full demo (collect → tamper → verify)
- `report.py` – Judge-friendly report
- `test_db.py` – Edge case tests

## How to Run
```bash
python evidence.py collect samples/test_log.txt "Officer_A"
python evidence.py verify samples/test_log.txt
./demo.sh
python report.py
