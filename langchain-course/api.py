import os
import sys 
import argparse
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain

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

# test prompt
test_prompt = PromptTemplate(
        template = "write the test cases for the language {language} and {code}",
        input_variables = ["language", "code"])

# create code chain
code_chain = LLMChain(
        llm = llm,
        prompt = code_prompt)


# create a test chain
test_chain = LLMChain(
        llm = llm,
        prompt = test_prompt,
        output_key = "test"
        )

# results 
code_result = code_chain({
    "language": args.language,
    "task": args.task
    })

# creating final chain
final_chain = SequentialChain(
        chains = [code_chain, test_prompt],
        input_variables = ["language", "task"],
        output_variables = ["test", "code"]
        )

result = chain.invoke({
    "language": args.language,
    "task": args.task
    })

print(result)

