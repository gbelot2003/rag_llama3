from langchain_community.document_loaders import WebBaseLoader
from langchain_ollama import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
import os

def fetch_and_presist_article(url):
    messages = []
    local_embeddings = OllamaEmbeddings(model="phi3:latest")
    persist_directory = "db"

    if os.path.exists(persist_directory):
        vectors = Chroma(persist_directory=persist_directory, embedding_function=local_embeddings)
        messages.append(f"Loader the existen DB")
    else:
        vectors = Chroma(persist_directory=persist_directory, embedding_function=local_embeddings)
        messages.append(f"Created the Chrome database")

    loader = WebBaseLoader(url)
    messages.append(f"URL loaded")
    data = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
    all_splits = text_splitter.split_documents(data)

    vectors.add_documents(all_splits)
    messages.append(f"added to Chrome")

    #print(all_splits)
    return messages
    #return all_splits
    