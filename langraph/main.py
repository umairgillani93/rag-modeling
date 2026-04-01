import os 
import sys 
from typing import TypedDict, List
from dataclasses import dataclass
from langchain_core.messages import HumanMessage, AIMessage, BaseMessage
from langchain.chat_models import init_chat_model
from langchain.tools import tool
from langchain.agents import create_agent
from langgraph.graph import StateGraph


# An Agent is LLM with special tools
# It does reasoning on the basis of intermieditery steps
# Steps that lead to the final required results

MODEL = "mistral:7b"

class AgentState(TypedDict):
    messages: List[BaseMessage]
    final_response: "ResponseFormat"

@dataclass
class ResponseFormat:
    """Response schema for the agent."""
    answer: str
    model: str
    tokens_used: int


@tool('web_search')
def search_phones(query: str) -> str:
    """Searches the web for the given query."""
    return f"Result for query {query}";

model = init_chat_model(
        model = MODEL,
        model_provider = "ollama"
        )

agent = create_agent(
        model, 
        tools = [search_phones]
        )

def agent_node(state):
    return create_agent(
            model = model, 
            tools = [search_phones]
            )


def format_response_node(state: AgentState):
    ai_msg = state["messages"][-1]
    answer_text = ai_msg.content
    tokens = ai_msg.usage_metadata["total_tokens"]
    model = ai_msg.response_metadata["model"]

    response = ResponseFormat(
        answer=answer_text.strip(),
        model=model,
        tokens_used=tokens
    )

    return {"final_response": response}

graph = StateGraph(AgentState)
graph.add_node("agent", agent_node)
graph.add_node("formatter", format_response_node)

graph.set_entry_point("agent")
graph.add_edge("agent", "formatter")
app = graph.compile()

if __name__ == '__main__':


    response = app.invoke(
            {"messages": [
                HumanMessage(content = "Best smartphones under 100K PKR, excluding Chinese brands, you MUST use the relevant tool")
                ]})
    print(response['final_response'])




