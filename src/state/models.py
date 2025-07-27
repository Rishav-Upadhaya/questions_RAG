from typing import TypedDict, Annotated, Sequence
from langchain_core.messages import BaseMessage, SystemMessage, HumanMessage, ToolMessage
from operator import add as add_messages


class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]