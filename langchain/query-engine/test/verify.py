import os
from langchain.vectorstores import Chroma
from langchain.embeddings import OllamaEmbeddings

embeddings = OllamaEmbeddings()

db = Chroma(
        embedding_function = embeddings, 
        persist_directory = "./test-emb"
        )

res = db.similarity_search("what color is fire")

print(res[0].page_content)
