from dotenv import load_dotenv

from src.constants import CHUNK_SIZE, INDEX_NAME, PATH_RAW_FILES
from src.data.etl import run_etl

load_dotenv()

if __name__ == "__main__":
    run_etl(PATH_RAW_FILES, INDEX_NAME, CHUNK_SIZE)
