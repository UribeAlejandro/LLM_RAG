from langchain import hub, vectorstores
from langchain.llms.gpt4all import GPT4All
from langchain.schema import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough
from langchain.vectorstores import Pinecone

from src.data.utils import embeddings_model, vector_store_init


def load_retriever(index_name: str) -> vectorstores:
    """Load the retriever."""
    vector_store_init(index_name)
    embeddings = embeddings_model()
    vector_store = Pinecone.from_existing_index(index_name, embeddings)
    retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 5})

    return retriever


def create_rag_model(model_path: str, retriever: vectorstores) -> RunnablePassthrough:
    """Create a RAG model."""
    llm = GPT4All(model=model_path, max_tokens=5162, verbose=True, n_threads=3)
    prompt = get_prompt_template()

    rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()} | prompt | llm | StrOutputParser()
    )

    return rag_chain


def get_prompt_template() -> str:
    """Get a prompt template from the hub.

    Returns
    -------
    str
        The prompt template.
    """
    prompt = hub.pull("rlm/rag-prompt")

    return prompt


def format_docs(docs):
    """Format documents for RAG."""
    return "\n\n".join(doc.page_content for doc in docs)
