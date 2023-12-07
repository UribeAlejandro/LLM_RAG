import os
from typing import List

import pinecone
from langchain.document_loaders import DirectoryLoader
from langchain.embeddings import GPT4AllEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Pinecone
from langchain_core.documents import Document

from src.data.utils import vector_store_init


def extract(path: str) -> List[Document]:
    """Extract documents from source.

    Parameters
    ----------
    path: str
        Path to raw files
    Returns
    -------
    List[Document]
        List of documents
    """
    loader = DirectoryLoader(path=path, glob="*.md")
    documents = loader.load()
    return documents


def transform(documents: List[Document], chunk_size: int) -> List[Document]:
    """Transform documents.

    Parameters
    ----------
    documents: List[Document]
        List of documents
    chunk_size: int
        Chunk size for splitting documents
    Returns
    -------
    List[Document]
        List of documents
    """
    text_splitter = CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=0)
    texts = text_splitter.split_documents(documents)
    return texts


def load(texts: List[Document], embeddings: GPT4AllEmbeddings, index_name: str) -> None:
    """Generate embeddings and upload to destination.

    Parameters
    ----------
    texts: List[Document]
        List of documents
    embeddings: GPT4AllEmbeddings
        Embeddings model
    index_name: str
        Index name to be used for vector database
    """
    Pinecone.from_documents(texts, embeddings, index_name=index_name)


def run_etl(path_raw_files: str, index_name: str, chunk_size: int) -> None:
    """Run ETL.

    Parameters
    ----------
    path_raw_files: str
        Path to raw files
    index_name: str
        Index name to be used for vector database
    chunk_size: int
        Chunk size for splitting documents
    """
    documents = extract(path_raw_files)
    texts = transform(documents, chunk_size)
    embeddings = vector_store_init(index_name)
    load(texts, embeddings, index_name)
