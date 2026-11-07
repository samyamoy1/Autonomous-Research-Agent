
from research_agent.agent_graph import build_research_graph


def main():

    topic = input("\nEnter your research topic: ")

    initial_state = {
        "topic": topic,
        "sources": [],
        "research_round": 0,
        "research_quality": "",
        "missing_areas": [],
        "feedback": "",
        "additional_search_queries": [],
        "final_report": ""
    }

    app = build_research_graph()

    result = app.invoke(initial_state)

    print("\n========== RESEARCH COMPLETED ==========")
    print(result["final_report"])


if __name__ == "__main__":
    main()
