from langgraph.graph import StateGraph, END
from state import models
from agents import retriever_agent, call_llm, decider


AgentState = models.AgentState
take_action = retriever_agent.take_action

def rag_agent():
    graph = StateGraph(AgentState)
    graph.add_node("llm", call_llm.call_llm)
    graph.add_node("retriever_agent", take_action)

    graph.add_conditional_edges(
        "llm",
        decider.should_continue,
        {True: "retriever_agent", False: END}
    )
    graph.add_edge("retriever_agent", "llm")
    graph.set_entry_point("llm")

    rag_agent = graph.compile()

    return rag_agent