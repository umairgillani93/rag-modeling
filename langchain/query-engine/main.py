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

# create embeddings using Ollama
MODEL = "llama3"
embeddings = OllamaEmbeddings()

print(" >> using LLAMA3 8b embeddings..")

# split the text into smaller chunks
text_splitter = CharacterTextSplitter(
        chunk_size = 150,
        separator = "\n",
        chunk_overlap = 0
        )

# initiate the loader
loader = TextLoader("./facts.txt")

# create docs instance, to be used for embeddings
docs = loader.load_and_split(
        text_splitter = text_splitter)



# create a vector store
db = Chroma.from_documents(
        docs,
        embedding = embeddings,
        persist_directory="emb"
        )
print(" >>>>>>>>>> DONE >>>>>>>>")
