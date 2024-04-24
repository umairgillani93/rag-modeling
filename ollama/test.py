import langchain 
from langchain_community.llms import Ollama

print('imports done')

ll = Ollama(model = 'llama2')

print('>> calling inference')
print(ll.invoke('why sky is blue'))
