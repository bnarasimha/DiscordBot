import chromadb
from dotenv import load_dotenv
import os
import uuid
from bs4 import BeautifulSoup
from langchain_community.document_loaders import WebBaseLoader
#from langchain_community.document_loaders import SeleniumURLLoader

storage_path = os.getenv('STORAGE_PATH')
if storage_path is None:
    raise ValueError('STORAGE_PATH environment variable is not set')

client = chromadb.PersistentClient(path=storage_path)

collection = client.get_or_create_collection(name="paperspace_collection")


links = ["https://www.paperspace.com/about"
         "https://www.paperspace.com/",
         "https://www.paperspace.com/notebooks",
         "https://www.paperspace.com/machines",
         "https://www.paperspace.com/deployments",
         "https://blog.paperspace.com",
         "https://www.paperspace.com/professional-services",
         "https://www.paperspace.com/contact-sales",
         "https://www.paperspace.com/pricing",
         "https://status.paperspace.com",
         "https://www.paperspace.com/customers",
         "https://docs.digitalocean.com/products/paperspace/"
         ]

# urls = ["https://www.paperspace.com/pricing"]
# loader = SeleniumURLLoader(urls=urls)
# links = ["https://www.paperspace.com/about"]
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
    print(html.page_content)
    return html


docs = loader.load()

docs = list(map(cleanHtml, docs))
 
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















# #collection = client.get_or_create_collection(name="mycollection")
# collection = chroma_client.create_collection(name="mycollection")

# if collection.count() < 0:
#     collection.add(
#         documents=[
#    "This is a document about machine learning",
#    "This is another document about data science",
#    "A third document about artificial intelligence"
#   ],
#   metadatas=[
#    {"source": "test1"},
#    {"source": "test2"},
#    {"source": "test3"}
#   ],
#   ids=["id1", "id2", "id3"]
#  )

# # private endpoint if running http server (in that case, its fine):
# print(client.list_collections())


# results = collection.query(
#     query_texts=[
#         "This is a query about machine learning and data science"
#     ],
#     n_results=1
# )

# print(results)