import os
from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser

from langchain_chroma import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import RecursiveUrlLoader
from langchain_community.vectorstores.utils import filter_complex_metadata
from langchain_text_splitters import RecursiveCharacterTextSplitter

MODEL = "mistral"
model = Ollama(model=MODEL)
embeddings = OllamaEmbeddings(model=MODEL)

links = ["https://www.paperspace.com/about"
         "https://www.paperspace.com/",
         "https://www.paperspace.com/notebooks",
         "https://www.paperspace.com/machines",
         "https://www.paperspace.com/deployments",
         "https://blog.paperspace.com",
         "https://docs.digitalocean.com/products/paperspace",
         "https://www.paperspace.com/professional-services",
         "https://www.paperspace.com/contact-sales",
         "https://www.paperspace.com/pricing",
         "https://status.paperspace.com",
         "https://www.paperspace.com/customers",
         "https://docs.digitalocean.com/products/paperspace/"
         ]

loader = WebBaseLoader(["https://docs.digitalocean.com/products/paperspace/pricing"])

import html2text
def cleanHtml(html):
    html.page_content = html2text.html2text(html.page_content)
    html.page_content = html.page_content.replace("\n", " ")
    return html

docs = loader.load()

docs = map(cleanHtml, docs)


vectorstore = Chroma.from_documents(filter_complex_metadata(docs), embeddings)

retriever = vectorstore.as_retriever(search_type="mmr", search_kwargs={"k": 2})


template = """Answer the question based only on the following context:
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
    return chain.invoke({"question":query})