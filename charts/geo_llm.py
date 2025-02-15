'''
Title: Geo LLM
Description: This code is used to generate JavaScript code for Leaflet map based on user query text.
Author: Taewook Kang
Date: 2024-07-01
Email: laputa99999@gmail.com
License: MIT
'''
import os, re
import torch
from dotenv import load_dotenv
from typing import List
from typing_extensions import TypedDict
from langchain import hub
from langchain.globals import set_verbose, set_debug
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Chroma
from langchain_community.chat_models import ChatOllama
from langchain.prompts import PromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.output_parsers import StrOutputParser
from langchain.schema import Document

print(f'GPU available: {torch.cuda.is_available()}')

local_llm = 'gemma2' # gamma2 better than 'llama3.2' in javascript code generation
llm = ChatOllama(model=local_llm, temperature=0)  # format="json", 

def text_to_geo_code(query_text):
	prompt = " " + query_text

	prompt = PromptTemplate(
		template = """You are a Leaflet programmer. Make JavaScript code using the existed Leaflet map 'map' objectin HTML script section to run the code simply for executing the below user question. Don't make the map object, new function, new layer again. Just make code routine simply. No comments and HTML tag like ```javascript, script.
		Here is the user question: 
		{question}
		""",
		input_variables=["question"],
	)

	text_to_geo_chain = prompt | llm | StrOutputParser()
	generated_code = text_to_geo_chain.invoke({"question": query_text})
	generated_code = generated_code.replace("L.map('map')", "map")

	script_regex = r"<script>(.*?)</script>"
	match = re.search(script_regex, generated_code, re.DOTALL)  

	code = ''
	if match:  
		code = match.group(1).strip()  # Return the extracted code
	else:
		code = generated_code

	return code

# Example usage
# query_text = "Zoom in Seoul, South Korea and draw a circle with a radius of 10 kilo meters."
# javascript_code = text_to_geo_code(query_text)
# print(javascript_code)
