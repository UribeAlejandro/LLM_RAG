import os

import pinecone
from langchain.embeddings import GPT4AllEmbeddings

from src.constants import EMBEDDINGS_METRIC, INDEX_NAME, TEST_TEXTS


def vector_store_init(index_name: str) -> None:
    """Initialize vectorstore with embeddings model.

    Parameters
    ----------
    index_name: str
        Index name to be used for vector database

    Returns
    -------
    GPT4AllEmbeddings
        Embeddings model
    """
    if os.environ.get("PINECONE_API_KEY", None) is None:
        raise Exception("Missing `PINECONE_API_KEY` environment variable.")

    if os.environ.get("PINECONE_ENV", None) is None:
        raise Exception("Missing `PINECONE_ENVIRONMENT` environment variable.")

    pinecone.init(
        api_key=os.getenv("PINECONE_API_KEY"),
        environment=os.getenv("PINECONE_ENV"),
    )

    embeddings = embeddings_model()
    res = embeddings.embed_documents(TEST_TEXTS)

    if INDEX_NAME not in pinecone.list_indexes():
        pinecone.create_index(index_name, dimension=len(res[0]), metric=EMBEDDINGS_METRIC)


def embeddings_model() -> GPT4AllEmbeddings:
    """Load embeddings model.

    Returns
    -------
    GPT4AllEmbeddings
        Embeddings model
    """
    embeddings = GPT4AllEmbeddings()
    return embeddings
