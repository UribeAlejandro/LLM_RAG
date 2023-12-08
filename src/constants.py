CHUNK_SIZE = 1000
INDEX_NAME = "clementine-loka"

EMBEDDINGS_METRIC = "cosine"
EMBEDDINGS_DIM_GPT4ALL = 384
EMBEDDINGS_MODEL_PATH = "models/all-MiniLM-L6-v2-f16.gguf"

MODELS = {
    "llama": "meta-llama/Llama-2-7b-hf",
    "dolly-v2": "databricks/dolly-v2-3b",
}
MODEL_PATH = "models/orca-mini-3b-gguf2-q4_0.gguf"

PATH_RAW_FILES = "datasets/raw"
PATH_TEST_FILES = "datasets/test"

TEST_TEXTS = ["this is the first chunk of text", "then another second chunk of text is here"]
