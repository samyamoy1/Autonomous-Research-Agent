
from typing import TypedDict
from research_agent.research import collect_research
from research_agent.critic import evaluate_research
from research_agent.llm import generate_response
from langgraph.graph import StateGraph, START, END


class AgentState(TypedDict):
    topic: str
    sources: list
    research_round: int
    research_quality: str
    missing_areas: list
    feedback: str
    additional_search_queries: list
    final_report: str


def researcher_node(state: AgentState):

    print("\n========== RESEARCHER ==========")

    if state["research_round"] == 0:
        queries = [state["topic"]]
    else:
        queries = state["additional_search_queries"]

    new_sources = []

    for query in queries:
        print(f"\nSearching for: {query}")

        results = collect_research(query, max_sources=3)
        new_sources.extend(results)

    existing_urls = {
        source["url"] for source in state["sources"]
    }

    for source in new_sources:
        if source["url"] not in existing_urls:
            state["sources"].append(source)
            existing_urls.add(source["url"])

    print("\nTotal collected sources:", len(state["sources"]))

    return {
        "sources": state["sources"],
        "research_round": state["research_round"] + 1
    }


def critic_node(state: AgentState):

    print("\n========== AI CRITIC ==========")
    print("Evaluating collected research...")

    evaluation = evaluate_research(
        topic=state["topic"],
        sources=state["sources"]
    )

    print("\nResearch quality:", evaluation["research_quality"])
    print("Feedback:", evaluation["feedback"])

    print("\nMissing areas:")
    for area in evaluation["missing_areas"]:
        print("-", area)

    print("\nAdditional search queries:")
    for query in evaluation["additional_search_queries"]:
        print("-", query)

    return {
        "research_quality": evaluation["research_quality"],
        "missing_areas": evaluation["missing_areas"],
        "feedback": evaluation["feedback"],
        "additional_search_queries": evaluation["additional_search_queries"]
    }


def route_after_critic(state: AgentState):

    print("\n========== ROUTING DECISION ==========")

    if state["research_quality"] == "sufficient":
        print("Research is sufficient. Moving to final report.")
        return "final_report"

    if state["research_round"] >= 3:
        print("Maximum research rounds reached.")
        return "final_report"

    print("Research is insufficient. Researching again.")
    return "researcher"


def final_report_node(state: AgentState):

    print("\n========== FINAL REPORT ==========")
    print("Generating research report...")

    context = ""

    # Use only the first 10 sources to control input size.
    for i, source in enumerate(state["sources"][:10], start=1):

        context += f"""
Source {i}:
Title: {source['title']}
URL: {source['url']}
Content: {source['content'][:500]}
"""

    system_prompt = """
    You are an expert research report writer.

    Write a concise report using only the provided research.

    Include:
    1. Introduction
    2. Key findings
    3. Important trends
    4. Challenges and limitations
    5. Conclusion

    Keep the report around 500 words.
    Do not invent facts.
    Include source URLs wherever relevant.
    """

    user_prompt = f"""
    Research topic: {state['topic']}

    Collected research:
    {context}

    Critic feedback:
    {state['feedback']}

    Write the final research report.
    """

    report = generate_response(system_prompt, user_prompt)

    print("\nReport generated successfully!")

    return {"final_report": report}


def build_research_graph():

    graph = StateGraph(AgentState)

    graph.add_node("researcher", researcher_node)
    graph.add_node("critic", critic_node)
    graph.add_node("final_report", final_report_node)

    graph.add_edge(START, "researcher")
    graph.add_edge("researcher", "critic")

    graph.add_conditional_edges(
        "critic",
        route_after_critic,
        {
            "researcher": "researcher",
            "final_report": "final_report"
        }
    )

    graph.add_edge("final_report", END)

    return graph.compile()
