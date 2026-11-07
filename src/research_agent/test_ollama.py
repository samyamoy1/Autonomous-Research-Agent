
from research_agent.llm import generate_response

system_prompt = "You are a helpful AI assistant."

user_prompt = "Explain what an AI agent is in two sentences."

response = generate_response(system_prompt, user_prompt)

print("\n========== OLLAMA RESPONSE ==========\n")
print(response)
