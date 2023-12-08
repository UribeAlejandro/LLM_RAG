import pinecone
import pytest
from dotenv import load_dotenv
from langchain.embeddings import GPT4AllEmbeddings

from src.constants import EMBEDDINGS_DIM_GPT4ALL, EMBEDDINGS_METRIC, INDEX_NAME, PATH_TEST_FILES
from src.data.etl import extract, transform
from src.data.utils import embeddings_model, vector_store_init

load_dotenv()


@pytest.fixture(scope="session", autouse=True)
def init():
    """Initialize Pinecone client."""
    vector_store_init(INDEX_NAME)
    embeddings = embeddings_model()
    return embeddings


def test_init(init):
    """Check if the Pinecone client is initialized."""
    assert isinstance(init, GPT4AllEmbeddings)


def test_extract():
    """Check if the raw data is extracted."""
    documents = extract(PATH_TEST_FILES)
    assert len(documents) == 1


def test_transform():
    """Check if the raw data is transformed."""
    documents = extract(PATH_TEST_FILES)
    texts = transform(documents, 1000)
    assert len(texts) == 1


def test_index_name(init):
    """Check if the index is created."""
    assert INDEX_NAME in pinecone.list_indexes()


def test_dimension(init):
    """Check if the dimension of the embeddings is correct."""
    assert pinecone.describe_index(INDEX_NAME).dimension == EMBEDDINGS_DIM_GPT4ALL


def test_metric(init):
    """Check if the metric of the embeddings is correct."""
    assert pinecone.describe_index(INDEX_NAME).metric == EMBEDDINGS_METRIC
