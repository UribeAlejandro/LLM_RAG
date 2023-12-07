CHUNK_SIZE = 1000
INDEX_NAME = "clementine-loka"
EMBEDDINGS_METRIC = "cosine"
EMBEDDINGS_DIM_GPT4ALL = 384
EMBEDDINGS_MODEL_PATH = "models/all-MiniLM-L6-v2-f16.gguf"

PATH_RAW_FILES = "datasets/raw"

TEST_TEXTS = ["this is the first chunk of text", "then another second chunk of text is here"]

EVAL_QUESTIONS = [
    "What is SageMaker?",
    "What are all AWS regions where SageMaker is available?",
    "How to check if an endpoint is KMS encrypted?",
    "What are SageMaker Geospatial capabilities?",
]
