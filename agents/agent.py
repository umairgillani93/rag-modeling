import os 
from langchain import hub
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.tools.retriever import create_retriever_tool
from langchain_community.llms import Ollama
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.agents import AgentExecutor
from langchain.agents import create_tool_calling_agent

print(' >> done loading..')

URL = "https://www.cognition-labs.com/introducing-devin"
loader = WebBaseLoader(URL)

# load the document loader
docs = loader.load()

# split the documents
documents = RecursiveCharacterTextSplitter(
        chunk_size = 200, chunk_overlap = 200
        ).split_documents(docs)

documents = documents[:5]

# create embeddings object
embeddings = OllamaEmbeddings()

# create vector store
vector = FAISS.from_documents(documents, embeddings)

# create retriever object
retriever = vector.as_retriever()

# turn the retriever into the tool for agent to work
retriever_tool = create_retriever_tool(
        retriever,
        "devin-AI",
        "Search for information about devin-AI. For any question about devin-AI, you must use this tool!"
        )

# create search instance for real time online search
search = TavilySearchResults()

# create a list of tools
tools = [search, retriever_tool]

# create llm instance
print(' >> loading model..')
llm = Ollama(model = "llama2")

# define the prompt to guide the agent
prompt = hub.pull("hwchase17/openai-functions-agent")
print(f'prompt messages:\n {prompt.messages}')

# create the agent
# we need to choose the agent type first -> check agent types documentation for this.
agent = create_tool_calling_agent(llm, tools, prompt)

agent_executor = AgentExecutor(agent = agent, tools = tools, verbose = True)

# call the agent
print(agent_executor.invoke({"input": "hi"}))
