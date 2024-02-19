from functools import lru_cache

from dotenv import load_dotenv

from src.constants import INDEX_NAME, MODEL_PATH
from src.model.rag import create_rag_model, load_retriever

load_dotenv()


@lru_cache
def get_lmm():
    retriever = load_retriever(INDEX_NAME)
    rag_model = create_rag_model(MODEL_PATH, retriever)
    return rag_model
