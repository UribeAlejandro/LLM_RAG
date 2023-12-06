from dotenv import load_dotenv

from src.data.etl import extract, load, transform

load_dotenv()

if __name__ == "__main__":
    documents = extract()
    texts = transform(documents)
    load(texts)
