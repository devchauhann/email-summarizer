
# agent/agent.py
"""Simple ADK-style agent demo wrapper for the Daily Email Summarizer project.
This demo uses a deterministic local summarizer for reproducibility on Kaggle.
Replace `call_llm` with ADK LLM calls for production use.
"""
import json
from tools import fetch_unread_emails_fallback
from prompts import build_summary_prompt

def call_llm(prompt: str) -> str:
    """Mock LLM call: replace with real ADK client in production."""
    # Very simple deterministic mock response
    return '{"summary": "Mock summary generated.", "priority": "Medium", "reason": "Deterministic demo.", "actions": ["Read and respond if needed"]}'

def summarize_email(email: dict) -> dict:
    prompt = build_summary_prompt(email)
    resp_text = call_llm(prompt)
    try:
        parsed = json.loads(resp_text)
    except Exception:
        parsed = {"summary": resp_text, "priority": "Medium", "reason": "Parsing failed; mock response.", "actions": ["Read and respond if needed"]}
    return {
        "id": email.get("id"),
        "subject": email.get("subject"),
        "sender": email.get("sender"),
        "date": email.get("date"),
        "summary": parsed.get("summary"),
        "priority": parsed.get("priority"),
        "reason": parsed.get("reason"),
        "actions": parsed.get("actions"),
    }

def run(csv_path="../data/sample_emails.csv", out_json="daily_report.json"):
    emails = fetch_unread_emails_fallback(csv_path)
    results = []
    for e in emails:
        results.append(summarize_email(e))
    with open(out_json, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2)
    print('Wrote', out_json)


if __name__ == '__main__':
    run()
