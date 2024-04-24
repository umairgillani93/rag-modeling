import os 
import sys 
from langchain_community.document_loaders import PyPDFLoader
from ..config.constants import DATA_PATH
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import FAISS

loader = PyPDFLoader(DATA_PATH)

# this retreives the pdf document with page numbers
pages = loader.load_and_split()

# create embeddings
embeddings = OllamaEmbeddings(model = "llama2")

# create vector 
faiss_index = FAISS.from_documents(pages, embeddings)
docs = faiss_index.similarity_search("how will the document be engaged?", k = 2)

for doc in docs:
    print(str(doc.metadata["page"]) + ":" , doc.page_content[:3000])
