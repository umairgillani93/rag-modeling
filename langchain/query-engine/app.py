import os
import sys
from langchain_community.llms import Ollama
from langchain import hub
from langchain.prompts import (
        ChatPromptTemplate,
        HumanMessagePromptTemplate,
        MessagesPlaceholder
        )
from langchain_anthropic import ChatAnthropic

from langchain_community.chat_models.ollama import ChatOllama 
from langchain.agents import AgentExecutor, OpenAIFunctionsAgent
from langchain.agents.agent_types import AgentType
from langchain.agents.initialize import initialize_agent
from langchain.agents import create_tool_calling_agent
from langchain_experimental.llms.ollama_functions import OllamaFunctions
from langchain.agents import AgentExecutor
from lib import create_openai_functions_agent
from langchain.schema import SystemMessage
from tools.sql import run_query
from custom import LLMWrapper
#from tools.report import write_report_tool

with open('/home/umairgillani/claude_key.txt', 'r') as f:
    KEY = f.read().splitlines()[0]

print("[**] Import Successful")

# create a chat model
print(' >> downloading model ..')
chat = ChatAnthropic(model="claude-3-opus-20240229", temperature = 0, api_key = KEY)
#chat = ChatOllama(model = "llama3:latest")
print(' >> model downloaded\n')
print(chat)


# create a prompt
prompt = ChatPromptTemplate(
        messages = [
            #SystemMessage((content = f"you are an AI that has access to a SQLite database.\n" 
            #    f"The database has tables of: {tables}\n"
            #    "Do not make any assumptions about what table exist "
            #    "or what columns exist. Instead, use the 'describe_table' function")),
            HumanMessagePromptTemplate.from_template("{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad")
            ]
        )

# prompt = hub.pull("hwchase17/openai-functions-agent")

# creating agent
# agent = create_openai_functions_agent(
#         llm = chat,
#         tools = tools,
#         prompt = prompt
#         )

# create tools
tools = [run_query]


agent = create_tool_calling_agent(
        llm = chat,
        tools = tools,
        prompt = prompt
        #verbose = True
        )

agent_executor = AgentExecutor(
        agent = agent,
        tools = tools,
        verbsoe = True)

res = agent_executor.invoke({"input":"Give me top 5 products from table"})
print(res)


