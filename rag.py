from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser

from langchain_chroma import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores.utils import filter_complex_metadata
from retreive_documents import retriever

MODEL = "mistral"
model = Ollama(model=MODEL)
embeddings = OllamaEmbeddings(model=MODEL)


template = """You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. 
If you don't know the answer, just say that you don't know. Use three sentences maximum and keep the answer concise.

{context}

Question: {question}
"""
prompt = ChatPromptTemplate.from_template(template)
output_parser = StrOutputParser()

setup_and_retrieval = RunnableParallel(
    {"context": retriever, "question": RunnablePassthrough()}
)

chain = setup_and_retrieval | prompt | model | output_parser

def getResponse(query):
    print(retriever.invoke(query))
    response = chain.invoke(query)
    return response