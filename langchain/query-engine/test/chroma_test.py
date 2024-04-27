import os
import sys
from langchain.vectorstores import Chroma
from langchain.document_loaders import TextLoader 
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.base import Embeddings
from langchain.embeddings import OllamaEmbeddings

print('imports done')

loader = TextLoader("test_file.txt")
 
text_splitter = CharacterTextSplitter(
        chunk_size = 20,
        separator = "\n",
        chunk_overlap = 0
        ) 
 
docs = loader.load_and_split(
        text_splitter) 


embeddings = OllamaEmbeddings()

print('everything done')

db = Chroma.from_documents(
        docs, 
        embedding = embeddings,
        persist_directory = "test-emb" 
        )

print('done vectorizing..')

