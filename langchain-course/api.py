import os
import sys 
import argparse
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# initiate parser object we'll be using this later to 
# pass command line argument to our langchain model
parser = argparse.ArgumentParser()
parser.add_argument("--task", default = "return a list of numbers")
parser.add_argument("--language", default = "c++")
args = parser.parse_args()

# initialize llm
llm = Ollama(model = "llama2")

# define code prompt
code_prompt = PromptTemplate(
        template = "write a very short {language} funtion that will {task}",
        input_variables = ["language", "task"]
        )

# create code chain
code_chain = LLMChain(
        llm = llm,
        prompt = code_prompt)


# results 
result = code_chain({
    "language": args.language,
    "task": args.task
    })

