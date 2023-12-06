import os

import pinecone
import pytest
from dotenv import load_dotenv

from src.constants import EMBEDDINGS_DIM_GPT4ALL, EMBEDDINGS_METRIC, INDEX_NAME

load_dotenv()


@pytest.fixture(scope="session", autouse=True)
def init():
    """Initialize Pinecone client."""
    pinecone.init(
        api_key=os.getenv("PINECONE_API_KEY"),
        environment=os.getenv("PINECONE_ENV"),
    )
    yield


def test_index_name(init):
    """Check if the index is created."""
    assert INDEX_NAME in pinecone.list_indexes()


def test_dimension(init):
    """Check if the dimension of the embeddings is correct."""
    assert pinecone.describe_index(INDEX_NAME).dimension == EMBEDDINGS_DIM_GPT4ALL


def test_metric(init):
    """Check if the metric of the embeddings is correct."""
    assert pinecone.describe_index(INDEX_NAME).metric == EMBEDDINGS_METRIC