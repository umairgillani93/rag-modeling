import os
import sys 
from langchain_community.llms import Ollama
from langchain_community.embeddings import OllamaEmbeddings
from langchain.prompts import PromptTemplate
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma

#content = str(input(" Enter content: " ))
#
#if (content == "exit"):
#    sys.exit('exitting..')
#
#prompt = PromptTemplate.from_template(
#    "Tell me a {adjective} joke about {content}."
#)
#
#with open('./facts.txt', 'r') as f:
#    result = "\n".join(f.read().splitlines())

# create the prompt

#prompt = """ use the following facts to answer the following questions:
#    """ + "\n\n" + result + "\n\n" + content

embeddings = OllamaEmbeddings()

text_splitter = CharacterTextSplitter(
        separator = "\n",
        chunk_size = 200,
        chunk_overlap = 0
        )

loader = TextLoader("./facts.txt")
docs = loader.load_and_split(
        text_splitter = text_splitter)

db = Chroma.from_documents(
        docs,
        embedding = embeddings,
        persist_directory="emb"
        )
        

print('search results: \n')
result = db.similarity_search("give me a cool fact about word Dreamt",
    k = 2)

print(result)
