from state import models
from langchain_core.messages import BaseMessage, SystemMessage, HumanMessage, ToolMessage
# from llm import gemini
from tools.tools import get_tools
from utils import systemprompt

system_prompt = systemprompt.system_prompt()
llm = get_tools()[1]
AgentState = models.AgentState


def call_llm(state: AgentState) -> AgentState:
    """Function to call the LLM with the current state."""
    print("\n=== CALLING LLM ===")
    messages = list(state['messages'])
    messages = [SystemMessage(content=system_prompt)] + messages
    message = llm.invoke(messages)
    return {'messages': [message]}