
# Agent folder

This folder contains a simple ADK-style agent demo with:

- agent.py: main agent runner (mock LLM output for reproducibility)
- tools.py: CSV fallback email loader
- prompts.py: prompt templates

To run locally:

```
python agent/agent.py
```

This writes `daily_report.json` in the current directory.
