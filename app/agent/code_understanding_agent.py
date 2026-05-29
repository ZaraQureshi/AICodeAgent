from llm.openai_client import run_llm

def code_understanding_agent(file_tree: list, code_chunks: list) -> str:
    prompt = f"""
You are a senior software engineer onboarding onto a new codebase.

Repository file structure:
{chr(10).join(file_tree)}

Relevant code snippets:
{chr(10).join(code_chunks)}

Explain clearly:
1. What problem this system solves
2. Major components and their responsibilities
3. Main execution and data flows
4. Where complexity or tight coupling exists
5. Which areas require caution when modifying

Do NOT suggest improvements or refactors.
Focus only on understanding the system.
"""
    return run_llm(prompt)
