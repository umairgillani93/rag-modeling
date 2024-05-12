import os
from langchain_community.tools.tavily_search import TavilySearchResults

search = TavilySearchResults()


print(search.invoke("what is the weather in Haripur, Pakistan"))
