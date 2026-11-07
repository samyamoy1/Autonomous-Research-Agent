from typing import TypedDict
from langgraph.graph import StateGraph, START, END


class AgentState(TypedDict):
    research_round: int
    research_quality: str


# Node 1: Researcher
def researcher_node(state: AgentState):

    current_round = state["research_round"] + 1

    print(f"\nResearch round: {current_round}")
    print("Collecting more information...")

    return {
        "research_round": current_round
    }


# Node 2: Critic
def critic_node(state: AgentState):

    print("Evaluating research...")

    if state["research_round"] >= 2:
        print("Research is sufficient!")
        return {
            "research_quality": "good"
        }

    print("Research is insufficient!")

    return {
        "research_quality": "insufficient"
    }


# Decision function
def check_research(state: AgentState):

    if state["research_quality"] == "good":
        return "complete"

    return "research_again"


# Node 3: Final report
def final_report_node(state: AgentState):

    print("\nGenerating final research report...")

    return {}


# Build graph
graph = StateGraph(AgentState)

graph.add_node("researcher", researcher_node)
graph.add_node("critic", critic_node)
graph.add_node("final_report", final_report_node)

# Normal edges
graph.add_edge(START, "researcher")
graph.add_edge("researcher", "critic")

# Conditional edges
graph.add_conditional_edges(
    "critic",
    check_research,
    {
        "complete": "final_report",
        "research_again": "researcher"
    }
)

graph.add_edge("final_report", END)

# Compile and execute
app = graph.compile()

result = app.invoke({
    "research_round": 0,
    "research_quality": ""
})

print("\nFinal State:")
print(result)