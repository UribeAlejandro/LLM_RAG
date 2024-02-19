from dotenv import load_dotenv
from fastapi import FastAPI
from langserve import add_routes

from src.serving.utils import get_lmm

load_dotenv()

model = get_lmm()

app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple api server using Langchain's Runnable interfaces",
)


add_routes(app, model, path="/rag")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
