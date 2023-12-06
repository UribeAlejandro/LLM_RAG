from dotenv import load_dotenv

from src.data.etl import embeddings_from_documents, extract

load_dotenv()

if __name__ == "__main__":
    texts = extract()
    embeddings_from_documents(texts)
