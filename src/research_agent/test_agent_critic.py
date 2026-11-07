
from research_agent.agent_graph import researcher_node, critic_node


state = {
    "topic": "Future of Generative AI",
    "sources": [],
    "research_round": 0,
    "research_quality": "",
    "missing_areas": [],
    "feedback": "",
    "additional_search_queries": [],
    "final_report": ""
}

# First, collect research.
research_result = researcher_node(state)
state.update(research_result)

# Then, evaluate the research.
critic_result = critic_node(state)
state.update(critic_result)

print("\n========== FINAL STATE ==========")
print("Quality:", state["research_quality"])
print("Research rounds:", state["research_round"])
