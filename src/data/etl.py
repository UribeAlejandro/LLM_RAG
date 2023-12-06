import os
from typing import List

import pinecone
from langchain.document_loaders import DirectoryLoader
from langchain.embeddings import GPT4AllEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Pinecone
from langchain_core.documents import Document

from src.constants import EMBEDDINGS_DIM_GPT4ALL, EMBEDDINGS_METRIC, INDEX_NAME


def extract() -> List[Document]:
    """Extract datasets from source."""
    loader = DirectoryLoader(path="datasets/raw", glob="*.md")
    documents = loader.load()

    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(documents)

    return texts


def embeddings_from_documents(texts: List[Document]) -> None:
    """Generate embeddings and upload to destination."""
    embeddings = GPT4AllEmbeddings()

    pinecone.init(
        api_key=os.getenv("PINECONE_API_KEY"),
        environment=os.getenv("PINECONE_ENV"),
    )

    if INDEX_NAME not in pinecone.list_indexes():
        pinecone.create_index(INDEX_NAME, dimension=EMBEDDINGS_DIM_GPT4ALL, metric=EMBEDDINGS_METRIC)

    Pinecone.from_documents(texts, embeddings, index_name=INDEX_NAME)
