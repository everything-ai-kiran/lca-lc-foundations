# %%
from dotenv import load_dotenv

load_dotenv()

# %%
from langchain.tools import tool
from tavily import TavilyClient

web_client = TavilyClient()

@tool
def search_web(search_query: str):
    """Searches the web for requested information"""
    return web_client.search(search_query)

# %%
from langchain.chat_models import init_chat_model

model = init_chat_model(model="gpt-5-nano")

# %%
from langchain.agents import create_agent
# from langgraph.checkpoint.memory import InMemorySaver

system_prompt = """
You are a personal chef assistant.
You can help users find recipes, plan meals, and answer cooking-related questions.
You have access to a web search tool that you can use to find information online.
Use the tool when you need to look up information or find recipes for the user.
"""

agent = create_agent(
    model=model,
    tools=[search_web],
    system_prompt=system_prompt,
    # checkpointer=InMemorySaver()
)

# if __name__ == "__main__":
#     from typing import Any
#     from langchain.messages import HumanMessage
#     from pprint import pprint

#     config: Any = {
#         "configurable": {
#             "thread_id": "1"
#         }
#     }

#     message = HumanMessage(content=[
#         {
#             "type": "text",
#             "text": "Give me latest 5 best recipes for my pre-workout meal for resistance training out there. Provide me where you got those from. Also, keep it below 600 kCal"
#         }
#     ])

#     input_messages: Any = {
#         "messages": [message]
#     }

#     response = agent.invoke(input=input_messages, config=config)
#     pprint(response["messages"][-1].content)
