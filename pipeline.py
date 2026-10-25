import time
from agents import AUDITOR_PROMPT, SYNTHESIZER_PROMPT, WRITER_PROMPT, call_agent


def run_pipeline(query: str, verbose: bool = True) -> dict:
  """Executes the multi-agent debiasing pipeline."""
  results = {}

  if verbose:
    print(f"\n{'=' * 60}\nUSER QUERY: {query}\n{'=' * 60}")

  # Step 1: Initial Draft
  if verbose:
    print("\n[1/3] Generating Initial Draft...")
  t0 = time.time()
  draft = call_agent(WRITER_PROMPT, query)
  results["draft"] = draft
  if verbose:
    print(f"✓ Completed in {time.time() - t0:.2f}s")

  # Step 2: Bias Audit
  if verbose:
    print("\n[2/3] Auditing for Western / Infrastructure Bias...")
  t0 = time.time()
  audit_input = (
      f"ORIGINAL QUERY: {query}\n\nDRAFT TO AUDIT:\n{draft}\n\nIdentify Western"
      " assumptions or missing global contexts:"
  )
  critique = call_agent(AUDITOR_PROMPT, audit_input)
  results["critique"] = critique
  if verbose:
    print(f"✓ Completed in {time.time() - t0:.2f}s")
    print(f"\n--- AUDITOR CRITIQUE ---\n{critique}")

  # Step 3: Pluriversal Synthesis
  if verbose:
    print("\n[3/3] Synthesizing Debiased Response...")
  t0 = time.time()
  synthesis_input = (
      f"USER QUERY: {query}\n\nINITIAL DRAFT:\n{draft}\n\nBIAS AUDIT"
      f" CRITIQUE:\n{critique}\n\nRewrite into a comprehensive, debiased"
      " final response:"
  )
  final_output = call_agent(SYNTHESIZER_PROMPT, synthesis_input)
  results["final_output"] = final_output
  if verbose:
    print(f"✓ Completed in {time.time() - t0:.2f}s")
    print(f"\n{'=' * 60}\nFINAL DEBIASED OUTPUT\n{'=' * 60}\n{final_output}")

  return results