import langchain 
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

print('>> loading..')

llm = Ollama(model="llama2")

print('>> model loaded.\n')

# Let's call it with prompt templatse now
# Prompt templates help LLM understand the raw input from user
# Passing some extract piece of information

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are world class technical documentation writer."),
    ("user", "{input}")
])


# Let's now chain the prompt with our LLM
##chain = prompt | llm 

# Let's invoke it with the same question now.
#print(chain.invoke({"input": "how can langsmith help with testing?"}))

# Let's parse the output and create a clear string of LLM response

output_parser = StrOutputParser()

chain = prompt | llm | output_parser

print('>> calling inference..')
print(chain.invoke({"input": "how can langsmith help with testing?"}))

