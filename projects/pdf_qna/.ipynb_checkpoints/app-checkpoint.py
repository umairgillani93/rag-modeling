import os
import sys 
from langchain_community.document_loaders import PyPDFLoader
from config.constants import DATA_PATH
from langchain_community.llms import Ollama
from langchain_community.embeddings import OllamaEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.vectorstores import FAISS
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain

# data loader path
loader = PyPDFLoader(DATA_PATH)

# this retreives the pdf document with page numbers
pages = loader.load_and_split()

# create embeddings
print(' >> creating embeddings')
embeddings = OllamaEmbeddings(model = "llama2")

# create model instance
llm = Ollama(model = "llama2")

# create a prompt template
prompt = ChatPromptTemplate.from_template(
        """Answer the following questions
        <context>
        {context}
        </context>

        Question: {input}"""
        )

# create vector 
print(' >> creating vector store')
vector = FAISS.from_documents(pages, embeddings)

# create retriever object
retriever = vector.as_retriever()

# create document chain
document_chain = create_stuff_documents_chain(llm, prompt)

# create retrieval chain
retrieval_chain = create_retrieval_chain(retriever, document_chain)

# define query
query = str(input('Enter query? '))
query_dict = {"input": query}


response = retrieval_chain.invoke(query_dict)

print(response)
