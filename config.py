import os

# Ollama local endpoint configuration ($0 cost)
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434/v1")
OLLAMA_API_KEY = "ollama"  # Required by OpenAI SDK format, ignored by Ollama

# Default model (ensure you've run `ollama pull llama3.2`)
DEFAULT_MODEL = "llama3.2"