
from research_agent.llm import generate_response

system_prompt = """
You are a helpful AI assistant.
Explain technical concepts in simple language.
"""

user_prompt = """
What is Agentic AI?
Explain:
1. What it means.
2. How it works.
3. One real-world example.
"""

response = generate_response(
    system_prompt,
    user_prompt
)

print("\n========== GROQ LLM RESPONSE ==========\n")
print(response)
