
from research_agent.agent_graph import researcher_node


initial_state = {
    "topic": "Future of Generative AI",
    "sources": [],
    "research_round": 0,
    "research_quality": "",
    "missing_areas": [],
    "feedback": "",
    "additional_search_queries": [],
    "final_report": ""
}

result = researcher_node(initial_state)

print("\n========== RESEARCH RESULT ==========")
print("Research round:", result["research_round"])
print("Total sources:", len(result["sources"]))
