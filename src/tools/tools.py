from tools.retriever import retriever_tool
from llm import gemini

# module‑level LLM
base_llm = gemini.get_gemini()["llm"]
# retriever_tool = retriever.retriever_tool()

def get_tools():
    tools = [retriever_tool]

    # bind without shadowing
    bound_llm = base_llm.bind_tools(tools)

    tools_dict = {tool.name: tool for tool in tools}
    print("Registered tools:", list(tools_dict.keys()))
    return tools_dict, bound_llm
