import chromadb
from dotenv import load_dotenv
import os
import uuid
from bs4 import BeautifulSoup
from langchain_community.document_loaders import WebBaseLoader
#from langchain_community.document_loaders import SeleniumURLLoader

storage_path = os.getenv('CHROMADB_STORAGE_PATH')
if storage_path is None:
    storage_path = "/home/paperspace/Documents/chromadb"

client = chromadb.PersistentClient(path=storage_path)

collection = client.get_or_create_collection(name="paperspace_collection")

links = ["https://www.paperspace.com/",
"https://www.paperspace.com/pricing",
"https://www.paperspace.com/notebooks",
"https://www.paperspace.com/machines",
"https://www.paperspace.com/deployments",		
"https://www.paperspace.com/artificial-intelligence",
"https://www.paperspace.com/gradient",
"https://www.paperspace.com/gradient/workflows",
"https://www.paperspace.com/gradient/deployments",		
"https://www.paperspace.com/gradient/pricing",	
"https://www.paperspace.com/gradient/cli",	
"https://www.paperspace.com/gradient/enterprise",
"https://www.paperspace.com/gradient/all-solutions",
"https://www.paperspace.com/products",
"https://www.paperspace.com/core",	
"https://www.paperspace.com/paperspace-ai-ml-cloud",
"https://www.paperspace.com/paperspace-vs-san-francisco-compute",
"https://www.paperspace.com/paperspace-vs-microsoft-azure",
"https://www.paperspace.com/paperspace-vs-crusoe",
"https://www.paperspace.com/paperspace-vs-lambda-labs",
"https://www.paperspace.com/paperspace-vs-coreweave",
"https://www.paperspace.com/alternative-to-colab-pro",
"https://www.paperspace.com/paperspace-vs-sagemaker",
"https://www.paperspace.com/deployment",	
"https://www.paperspace.com/gpu",
"https://www.paperspace.com/faq-cloud-gpu",
"https://www.paperspace.com/a100-gpus",
"https://www.paperspace.com/h100-gpus-are-available-now",
"https://www.paperspace.com/a6000-gpus-are-available-now",		
"https://www.paperspace.com/gpu-cloud-machine-learning",	
"https://www.paperspace.com/computer-vision",
"https://www.paperspace.com/natural-language-processing",
"https://www.paperspace.com/professional-services",
"https://www.paperspace.com/gpu-cloud-comparison",	
"https://www.paperspace.com/gpu-cloud-comparison",
"https://www.paperspace.com/about",
"https://www.paperspace.com/careers",
"https://www.paperspace.com/contact-sales",
"https://www.paperspace.com/business",
"https://www.paperspace.com/security",
"https://www.paperspace.com/download-app",
"https://www.paperspace.com/gpu-cloud-built-for-machine-learning",
"https://www.paperspace.com/deepfakes",
"https://www.paperspace.com/nvidia-h100",
"https://www.paperspace.com/customers",
"https://www.paperspace.com/nvidia-csp-partner",
"https://www.paperspace.com/advanced-technologies-group",
"https://www.paperspace.com/graphcore-2",
"https://www.paperspace.com/legal",
"https://www.paperspace.com/legal/acceptable-use-policy",
"https://www.paperspace.com/legal/terms-of-service",
"https://www.paperspace.com/legal/privacy-policy"]

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













# links = ["https://www.paperspace.com/about"
#          "https://www.paperspace.com/",
#          "https://www.paperspace.com/notebooks",
#          "https://www.paperspace.com/machines",
#          "https://www.paperspace.com/deployments",
#          "https://blog.paperspace.com",
#          "https://www.paperspace.com/professional-services",
#          "https://www.paperspace.com/contact-sales",
#          "https://www.paperspace.com/pricing",
#          "https://status.paperspace.com",
#          "https://www.paperspace.com/customers",
#          "https://docs.digitalocean.com/products/paperspace/"
#          ]

# urls = ["https://www.paperspace.com/pricing"]
# loader = SeleniumURLLoader(urls=urls)
# links = ["https://www.paperspace.com/about"]