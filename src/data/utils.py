import os

import pinecone
from langchain.embeddings import GPT4AllEmbeddings

from src.constants import EMBEDDINGS_METRIC, EMBEDDINGS_MODEL_PATH, INDEX_NAME, TEST_TEXTS


def vector_store_init(index_name: str) -> GPT4AllEmbeddings:
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
    embeddings = GPT4AllEmbeddings(model=EMBEDDINGS_MODEL_PATH)
    res = embeddings.embed_documents(TEST_TEXTS)

    pinecone.init(
        api_key=os.getenv("PINECONE_API_KEY"),
        environment=os.getenv("PINECONE_ENV"),
    )

    if INDEX_NAME not in pinecone.list_indexes():
        pinecone.create_index(index_name, dimension=len(res[0]), metric=EMBEDDINGS_METRIC)

    return embeddings
