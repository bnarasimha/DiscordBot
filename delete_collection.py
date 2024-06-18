import chromadb
from dotenv import load_dotenv
import os

load_dotenv('.env.local')

storage_path = os.getenv('STORAGE_PATH')
if storage_path is None:
    raise ValueError('STORAGE_PATH environment variable is not set')

client = chromadb.PersistentClient(path=storage_path)

client.delete_collection(name="paperspace_collection")