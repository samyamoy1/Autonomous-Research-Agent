from typing import TypedDict
from langgraph.graph import StateGraph, START, END


class AgentState(TypedDict):
    research_quality: str
    result: str


# Node 1
def researcher_node(state: AgentState):
    print("\nResearching topic...")

    return {
        "result": "Research completed"
    }


# Node 2
def critic_node(state: AgentState):
    print("Evaluating research...")

    return {
        "research_quality": "good"
    }


# Decision function
def check_research(state: AgentState):

    if state["research_quality"] == "good":
        return "complete"

    else:
        return "research_again"


# Node 3
def final_report_node(state: AgentState):
    print("Generating final report...")

    return {
        "result": "Final report generated!"
    }


# Node 4
def research_again_node(state: AgentState):
    print("Researching again...")

    return {
        "result": "Additional research completed"
    }


# Build graph
graph = StateGraph(AgentState)

graph.add_node("researcher", researcher_node)
graph.add_node("critic", critic_node)
graph.add_node("final_report", final_report_node)
graph.add_node("research_again", research_again_node)

graph.add_edge(START, "researcher")
graph.add_edge("researcher", "critic")

# Conditional routing
graph.add_conditional_edges(
    "critic",
    check_research,
    {
        "complete": "final_report",
        "research_again": "research_again"
    }
)

graph.add_edge("final_report", END)
graph.add_edge("research_again", END)

app = graph.compile()

result = app.invoke({
    "research_quality": "",
    "result": ""
})

print("\nFinal State:")
print(result)