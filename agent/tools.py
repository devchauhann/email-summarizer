
# agent/tools.py
import csv
from typing import List, Dict

def fetch_unread_emails_fallback(csv_path: str) -> List[Dict]:
    rows = []
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for r in reader:
            rows.append({
                'id': r.get('id'),
                'subject': r.get('subject'),
                'sender': r.get('sender'),
                'body': r.get('body'),
                'date': r.get('date')
            })
    return rows
