import os 
import sys 
from langchain_core.messages import HumanMessage
from langchain.chat_models import init_chat_model
from langchain.tools import tool
from langchain.agents import create_agent


# An Agent is LLM with special tools
# It does reasoning on the basis of intermieditery steps
# Steps that lead to the final required results

@tool('web_search')
def search_phones(query: str) -> str:
    """Searches the web for the given query."""
    return f"Result for query {query}";
        

model = init_chat_model(
        model = "mistral:7b",
        model_provider = "ollama"
        )


agent = create_agent(
        model = model, 
        tools = [search_phones]
        )

response = agent.invoke(
        {"messages": [
            HumanMessage(content = "Best smartphones under 100K PKR, excluding Chinese brands, you MUST use the relevant tool")
            ]})

print(response)



