import os 
from langchain.vectorstores import Chroma
from langchain.embeddings import OllamaEmbeddings

embeddings = OllamaEmbeddings()

db = Chroma(
        embedding_function = embeddings,
        persist_directory = "emb"
        )

res = db.similarity_search("what is an interesting fact about english language", k = 1)

print(res[0].page_content)
