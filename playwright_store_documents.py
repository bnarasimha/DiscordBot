import os
import uuid
import chromadb
from langchain.document_loaders import PlaywrightURLLoader

storage_path = os.getenv('CHROMADB_STORAGE_PATH')
if storage_path is None:
    raise ValueError('CHROMADB_STORAGE_PATH environment variable is not set')

client = chromadb.PersistentClient(path=storage_path)

collection = client.get_or_create_collection(name="playwright_paperspace_collection")
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
loader = PlaywrightURLLoader(urls=links, remove_selectors=["header", "footer"])

docs = loader.load()

for doc in docs:
    print(doc.page_content)
    collection.upsert(
        ids=[str(uuid.uuid1())], metadatas=doc.metadata, documents=doc.page_content
    )