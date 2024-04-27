import os
import sys 
from langchain_community.embeddings import OllamaEmbeddings
from langchain.vectorstores import Chroma

embeddings = OllamaEmbeddings()
db = Chroma(persist_directory = "emb", embedding_function = embeddings)

emb = embeddings.embed_query("english language")

result = db.similarity_search_by_vector(emb)

print(result)

