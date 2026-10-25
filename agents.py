from config import DEFAULT_MODEL, OLLAMA_API_KEY, OLLAMA_BASE_URL
from openai import OpenAI

# OpenAI SDK configured for local Ollama daemon
client = OpenAI(base_url=OLLAMA_BASE_URL, api_key=OLLAMA_API_KEY)

# ---------------------------------------------------------------------------
# System Prompts
# ---------------------------------------------------------------------------
WRITER_PROMPT = """
You are an initial drafting assistant. Answer the user's prompt clearly, 
focusing on providing a solid, practical baseline response.
"""

AUDITOR_PROMPT = """
You are an expert Cultural & Systems Auditor trained to identify Western and Eurocentric bias.
Critique the provided draft for:
1. Unstated infrastructure assumptions (e.g., high bandwidth, continuous grid power, high smartphone adoption).
2. Western legal, corporate, or economic norms (e.g., individualism over collective community systems, US/EU regulatory defaults).
3. Epistemic bias (ignoring non-Western practices, indigenous knowledge systems, or Global South realities).

Provide a concise, bulleted list of 2-3 specific blind spots in the draft.
"""

SYNTHESIZER_PROMPT = """
You are a Pluriversal Editor. Your job is to rewrite the initial draft by 
seamlessly incorporating the auditor's critique.
Ensure the final output offers a globally balanced, adaptable solution without 
treating Western defaults as universal standard practice.
"""


# ---------------------------------------------------------------------------
# Helper execution function
# ---------------------------------------------------------------------------
def call_agent(
    system_prompt: str, user_content: str, model: str = DEFAULT_MODEL
) -> str:
  """Calls the local LLM endpoint via OpenAI format."""
  response = client.chat.completions.create(
      model=model,
      messages=[
          {"role": "system", "content": system_prompt},
          {"role": "user", "content": user_content},
      ],
      temperature=0.3,
  )
  return response.choices[0].message.content