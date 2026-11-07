from research_agent.rag import answer_question


question = input("\nAsk a question about your research: ")

answer = answer_question(question)

print("\n========== ANSWER ==========\n")
print(answer)