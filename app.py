import sys
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = Ollama(model = "llama2")

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are the best school level teacher who can explain mathematical concepts very well."),
    ("user", "{input}")
])

output_parser = StrOutputParser()

chain = prompt | llm | output_parser

print(chain.invoke({"input": "explain integration with some examples"}))

