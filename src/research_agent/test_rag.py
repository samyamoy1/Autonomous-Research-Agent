from research_agent.research import collect_research
from research_agent.rag import answer_question


topic = "Retrieval Augmented Generation"

print("\nCollecting research sources...")

sources = collect_research(topic, max_sources=3)

question = "What is RAG and how does it work?"

print("\nGenerating answer...")

answer = answer_question(question, sources)

print("\n========== FINAL ANSWER ==========\n")
print(answer)