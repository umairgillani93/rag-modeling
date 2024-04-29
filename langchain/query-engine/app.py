import os
import sys
from langchain_community.llms import Ollama
from langchain.prompts import (
        ChatPromptTemplate,
        HumanMessagePromptTemplate,
        MessagesPlaceholder
        )
from sql import run_query
from langchain.agents import AgentExecutor 
from langchain.agents.agent_types import AgentType
from langchain.agents.initialize import initialize_agent
from langchain.agents import create_tool_calling_agent
from langchain_experimental.llms.ollama_functions import OllamaFunctions

print("[**] Import Successful")

# create a chat model
chat = Ollama(model="llama3")

# create a prompt
prompt = ChatPromptTemplate(
        messages = [
            HumanMessagePromptTemplate.from_template("{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad")
            ]
        )


# define the tools 
tools = [run_query]

# creating agent
agent = OllamaFunctions(
        llm = chat,
        prompt = prompt,
        tools = tools,
        )
print(type(agent))

input_dict = {"agent": agent,
            "tools": tools}
                  
agent_executor = AgentExecutor(input_dict)        

print(agent_executor("How many users are in the database?"))

