import os
import sys
from langchain.prompts import HumanMessagePromptTemplate
from langchain.prompts import ChatPromptTemplate
from langchain_community.chat_models.ollama import ChatOllama 
from langchain_community.embeddings import OllamaEmbeddings
from langchain.chains import LLMChain

'''
so we are going to build a chat-system now in a gpt-playgound style
and we know we need 3 components for this

  1 - HumanMessaage (which is what human is going to pass as a content with some extra template text)
  2 - ChatMessage (which is going to be the response of Chat bot)
  3 - SystemMessage (which is something we pass the model to get some idea that how exactly we need our bot to answer questions)

'''

# our prompt we are going to pass the LLM
prompt = ChatPromptTemplate(
        # This is going to have input_variables
        input_variables = ['content'],
        # Lets pass the messages input to
        # Initially we have embedd any prompt we're passing whatever content we are getting
        # from user directly to the chat model
        messages = [
            HumanMessagePromptTemplate.from_template("{content}")
            ]
        )


# lets create a language model now
# since we're building a chat style application so we need to import ChatOllama model
# instead of Ollama
chat = ChatOllama(model = "llama2")

# create our embeddings
embeddigns = OllamaEmbeddings()

# define our chain
chain = LLMChain(
        llm = chat,
        prompt = prompt
        )

# start infinite loop
while True:
    content = str(input(">> "))
    print(f'your content: {content}')

    if (content == 'exit'):
        sys.exit('exitting..')

    result = chain({"content": content})
    print(result['text'])

