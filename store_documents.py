import chromadb
from dotenv import load_dotenv
import os
import uuid
from bs4 import BeautifulSoup
from langchain_community.document_loaders import WebBaseLoader

storage_path = os.getenv('CHROMADB_STORAGE_PATH')
if storage_path is None:
    storage_path = "/home/paperspace/Documents/chromadb"

client = chromadb.PersistentClient(path=storage_path)

collection = client.get_or_create_collection(name="gpudroplet_collection")

links = ["https://www.digitalocean.com/products/gpu-droplets/"]

loader = WebBaseLoader(links)

import html2text
def cleanHtml(html):
    html.page_content = html2text.html2text(html.page_content)
    html.page_content = html.page_content.replace("\n", " ")
    html.page_content = html.page_content.replace("Ä¢", " ")
    html.page_content = html.page_content.replace("¬†", " ")
    html.page_content = html.page_content.replace("Â", " ")
    html.page_content = html.page_content.replace("â€", " ")
    html.page_content = html.page_content.replace("�", " ")
    html.page_content = html.page_content.replace("?", "? ")
    html.page_content = html.page_content.replace("Äç", " ")
    html.page_content = html.page_content.replace("Äî", " ")
    return html


docs = loader.load()

docs = list(map(cleanHtml, docs))
 
for doc in docs:
    print(doc.page_content)
    collection.upsert(
        ids=[str(uuid.uuid1())], metadatas=doc.metadata, documents=doc.page_content
    )


#Load PDF files in a directory
from langchain_community.document_loaders import PyPDFDirectoryLoader

loader = PyPDFDirectoryLoader("pdfs/")
docs = loader.load()
for doc in docs:
    print(doc.page_content)
    collection.upsert(
        ids=[str(uuid.uuid1())], metadatas=doc.metadata, documents=doc.page_content
    )


# results = collection.query(
#     query_texts=["what is the price of VPN Gateway?"], 
#     n_results=1 
# )

#print(collection.count())