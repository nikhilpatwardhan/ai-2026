# Overview
How to query a local LLM using Ollama for OCR and/or text.

# Pre-requisities
Install Ollama
https://ollama.com/download

Install the below models:
- glm-ocr:latest
- smollm2:latest

# How to run
```
uv run .\llm\glm_ocr.py
uv run .\llm\model_chat.py
uv run .\main.py
```