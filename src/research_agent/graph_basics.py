from typing import TypedDict
from langgraph.graph import StateGraph, START, END


# Define our shared state
class AgentState(TypedDict):
    message: str


# Node 1
def greeting_node(state: AgentState):
    print("Greeting node executed!")

    return {
        "message": state["message"] + " Welcome to LangGraph!"
    }


# Node 2
def response_node(state: AgentState):
    print("Response node executed!")

    return {
        "message": state["message"] + " Let's build an AI agent."
    }


# Create graph
graph = StateGraph(AgentState)

# Add nodes
graph.add_node("greeting", greeting_node)
graph.add_node("response", response_node)

# Add edges
graph.add_edge(START, "greeting")
graph.add_edge("greeting", "response")
graph.add_edge("response", END)

# Compile graph
app = graph.compile()


# Run graph
result = app.invoke({
    "message": "Hello!"
})

print("\nFinal result:")
print(result)