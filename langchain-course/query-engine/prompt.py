import os 
import sys 
from langchain import hub
from langchain.embeddings import OllamaEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain_community.chat_models.ollama import ChatOllama
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain

# input query
query = "what is an interesting fact about English language"

# create embeddings
embeddings = OllamaEmbeddings(model = "llama3")

# create a vectore store to convert query into query_embeddgns
db = Chroma(
        persist_directory = "emb",
        embedding_function = embeddings
        )

# create chat models instance
chat = ChatOllama(model = "llama3")

# create retriever instance
retriever = db.as_retriever()

# initiate retriever object
# what this does is it uses RetrieverQA to create LLM chain
# having SystemMessage, HumanMessage and ChatTemplate all setup for us
# in a Q/A kind of fashion
# so instead of using our own chain, we can use RetrieverQA directly

# create retriever instance
#retriever = db.as_retriever()
#retrieval_qa_chat_prompt = hub.pull("langchain-ai/retrieval-qa-chat")
#
#combine_docs_chain = create_stuff_documents_chain(
#    chat, retrieval_qa_chat_prompt
#)
#retrieval_chain = create_retrieval_chain(retriever, combine_docs_chain)
#
#result = retrieval_chain.invoke({"input": query}) 
#
#print(result)


chain = RetrievalQA.from_llm(
        llm = chat,
        retriever = retriever
        #chat_type = "stuff"
        )


# generate results from defined model
result = chain.run(query)

print(result)
