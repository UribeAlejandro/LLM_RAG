import os
from typing import List

import pinecone
from langchain.document_loaders import DirectoryLoader
from langchain.embeddings import GPT4AllEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Pinecone
from langchain_core.documents import Document

from src.constants import CHUNK_SIZE, EMBEDDINGS_METRIC, INDEX_NAME


def extract() -> List[Document]:
    """Extract documents from source."""
    loader = DirectoryLoader(path="datasets/raw", glob="*.md")
    documents = loader.load()
    return documents


def transform(documents: List[Document]) -> List[Document]:
    """Transform documents."""
    text_splitter = CharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=0)
    texts = text_splitter.split_documents(documents)
    return texts


def load(texts: List[Document]) -> None:
    """Generate embeddings and upload to destination."""
    embeddings = GPT4AllEmbeddings()
    test_texts = ["this is the first chunk of text", "then another second chunk of text is here"]

    res = embeddings.embed_documents(test_texts)

    pinecone.init(
        api_key=os.getenv("PINECONE_API_KEY"),
        environment=os.getenv("PINECONE_ENV"),
    )

    if INDEX_NAME not in pinecone.list_indexes():
        pinecone.create_index(INDEX_NAME, dimension=len(res[0]), metric=EMBEDDINGS_METRIC)

    Pinecone.from_documents(texts, embeddings, index_name=INDEX_NAME)
