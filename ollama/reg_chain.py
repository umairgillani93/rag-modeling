import os 
import sys 
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain 
from langchain_community.llms import Ollama
from langchain.chains import create_retrieval_chain

print('>> imports done')

# Get URL
URL = "https://devinai.ai/"

# Load the page-content
loader = WebBaseLoader(URL)

# Create a docs object
docs = loader.load()

# Create page-content vector embeddings to store in VectorStore
embeddings = OllamaEmbeddings()

# Create LLM object
llm = Ollama(model = "llama2")

# Print llm configuration
print(llm.show_config())

# NOw via these embeddings we'll ingest the data to VectorStore
# Let's use a simple VectorStore called FAISS

# Build our index first this will take the following steps
# 1 - Split text characters
# 2 - Split the documents 
# 3 - Pass documents and embeddings to FAISS VectorStore

text_splitter = RecursiveCharacterTextSplitter()
documents = text_splitter.split_documents(docs)
vector = FAISS.from_documents(documents, embeddings)

# Since our data is indexed into VectorStore now let's create a retrievel chain 
# This chain will take incoming questions
# Look into existing VectorStore for relevant documents 
# Then pass this document, along with original query from user to LLM and get the respones


prompt = ChatPromptTemplate.from_template("""Answer the following question

        <context>
        {context}
        </context>


        Question: {input}""")

document_chain = create_stuff_documents_chain(llm, prompt)

# Now will will dynamically select the most relevant document with our query 
# And hence will pass the LLM for response

# Create a "retriever" object
print('\n>> creating retrievel chain..')
retriever = vector.as_retriever()
retrieval_chain = create_retrieval_chain(retriever, document_chain)

# Define input query
input_query = "What is devin? explain in detail?"

# Let's invoke the chain now
invoke_dict = {"input": input_query}
print('\n>> invoking response..')
response = retrieval_chain.invoke(invoke_dict)

print(response["answer"])
print('\n')
print(response.keys())
