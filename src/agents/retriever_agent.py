from state import models
from tools import tools
from agents import decider
from langchain_core.messages import ToolMessage

AgentState = models.AgentState
tools_dict = tools.get_tools()[0]


def take_action(state: AgentState) -> AgentState:
    """Execute tool calls from the LLM's response."""

    tool_calls = state['messages'][-1].tool_calls
    print(f"\n=== TOOL CALLS ===\n")
    results = []
    for t in tool_calls:
        tool_name = t['name'].strip()
        if tool_name not in tools_dict:
            print(f"\nTool: {tool_name} does not exist.")
            result = "Incorrect Tool Name, Please Retry and Select tool from List of Available tools."
        else:
            result = tools_dict[tool_name].invoke(t['args'].get('query', ''))
            print(f"Result length: {len(str(result))}")
        results.append(ToolMessage(tool_call_id=t['id'], name=tool_name, content=str(result)))

    print("Tools Execution Complete. Back to the model!")
    return {'messages': results}