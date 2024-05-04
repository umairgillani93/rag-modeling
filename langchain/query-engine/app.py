import os
import sys
from langchain_community.llms import Ollama
from langchain import hub
from langchain.prompts import (
        ChatPromptTemplate,
        HumanMessagePromptTemplate,
        MessagesPlaceholder
        )
from sql import run_query, list_tables
from langchain.agents import AgentExecutor, OpenAIFunctionsAgent
from langchain.agents.agent_types import AgentType
from langchain.agents.initialize import initialize_agent
from langchain.agents import create_tool_calling_agent
from langchain_experimental.llms.ollama_functions import OllamaFunctions
from langchain.agents import AgentExecutor
from lib import create_openai_functions_agent
from langchain.schema import SystemMessage


print("[**] Import Successful")

# create a chat model
#chat = ChatOpenAI()

# call tables functions
tables = list_tables()

# create a prompt
prompt = ChatPromptTemplate(
        messages = [
            SystemMessage(content = f"you are an AI that has access to a SQLite database. {tables}"),
            HumanMessagePromptTemplate.from_template("{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad")
            ]
        )

# prompt = hub.pull("hwchase17/openai-functions-agent")


# define the tools 
tools = [run_query]

# creating agent
# agent = create_openai_functions_agent(
#         llm = chat,
#         tools = tools,
#         prompt = prompt
#         )


agent = create_openai_functions_agent(
        llm = chat,
        tools = tools,
        prompt = prompt
        )

agent_executor = AgentExecutor(
        agent = agent, 
        tools = tools
        )

print(agent_executor)
                  
#print(agent_executor.invoke({"input":"what is langchain?"}))
