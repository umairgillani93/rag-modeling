import os
import sys
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.llms import Ollama
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
#from langchain_chroma import Chroma

print(' >> Import successful\n')

# load the text documents
docs = TextLoader('./data.txt').load()

# split the text
text_splitter = CharacterTextSplitter(chunk_size = 1, chunk_overlap = 0)

# preparing documents for vectore store
documents = text_splitter.split_documents(docs)

# creating vector store instance 'db' 
db = FAISS.from_documents(documents, OllamaEmbeddings())

# define query
query = "what is the data?"
docs = db.similarity_search(query)

#emb_vector = OllamaEmbeddings().embed_query(query)
