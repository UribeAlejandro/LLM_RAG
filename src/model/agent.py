import os

import pinecone
from langchain.chains import RetrievalQA
from langchain.embeddings import GPT4AllEmbeddings
from langchain.llms import GPT4All
from langchain.vectorstores import Pinecone

from src.constants import INDEX_NAME


def pinecone_init():
    pinecone.init(
        api_key=os.getenv("PINECONE_API_KEY"),
        environment=os.getenv("PINECONE_ENV"),
    )

    embeddings = GPT4AllEmbeddings()
    vectorstore = Pinecone.from_existing_index(INDEX_NAME, embeddings)

    return vectorstore


def build_chain(model: str, vectorstore: Pinecone):
    llm = GPT4All(model=model)
    qa = RetrievalQA.from_chain_type(
        llm=llm, chain_type="stuff", retriever=vectorstore.as_retriever(), return_source_documents=True
    )

    return qa
