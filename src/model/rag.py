from typing import Any

import langchain
from langchain import hub
from langchain.chains import RetrievalQA
from langchain.llms.gpt4all import GPT4All
from langchain.vectorstores import Pinecone

from src.data.utils import embeddings_model, vector_store_init


def load_retriever(index_name: str) -> langchain.vectorstores:
    vector_store_init(index_name)
    embeddings = embeddings_model()
    vector_store = Pinecone.from_existing_index(index_name, embeddings)
    retriever = vector_store.as_retriever(
        search_type="similarity_score_threshold", search_kwargs={"score_threshold": 0.8}
    )

    return retriever


def create_rag_model(model_path: str, retriever: langchain.vectorstores, **kwargs) -> RetrievalQA:
    llm = GPT4All(model=model_path)
    prompt = get_prompt_template()

    qa_chain = RetrievalQA.from_chain_type(
        llm, chain_type="stuff", verbose=True, retriever=retriever, chain_type_kwargs={"prompt": prompt}, **kwargs
    )

    return qa_chain


def get_prompt_template(template_name: str = "rlm/rag-prompt") -> Any:
    """Get a prompt template from the hub.

    Parameters
    ----------
    template_name : str
        Name of the template to get from the hub.

    Returns
    -------
    str
        The prompt template.
    """
    prompt = hub.pull(template_name)

    return prompt
