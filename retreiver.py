from langchain_chroma import Chroma

from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings

llm = "mistral"
embeddings = OllamaEmbeddings(model=llm)

loader = WebBaseLoader("https://blog.paperspace.com/grounding-dino-1-5-pushing-the-boundaries-of-open-set-object-detection/")
docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_documents(docs)
vectorstore = Chroma.from_documents(documents=splits, embedding=embeddings)

retriever = vectorstore.as_retriever()


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)