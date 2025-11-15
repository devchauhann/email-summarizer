
# agent/prompts.py
def build_summary_prompt(email: dict) -> str:
    body_snippet = (email.get('body') or '')[:800]
    prompt = (
        f"You are a succinct email assistant.\n"
        f"Email subject: {email.get('subject')}\n"
        f"From: {email.get('sender')}\n"
        f"Body snippet: {body_snippet}\n\n"
        "Generate: 1) A one-sentence summary, 2) Priority (High/Medium/Low) with a one-line reason,"        " and 3) up to 3 action items as bullet points. Provide output in JSON with keys: summary, priority, reason, actions."
    )
    return prompt
