from langchain_community.vectorstores import FAISS
from langchain_community.llms import Cohere
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
import os

# Load Cohere API key from .env
load_dotenv()
cohere_key = os.getenv("COHERE_API_KEY")

def answer_question(doc_text, question):
    # Split document into chunks
    splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = splitter.split_text(doc_text)

    # ✅ Use HuggingFaceEmbeddings to avoid CohereEmbeddings bug
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectordb = FAISS.from_texts(chunks, embedding=embeddings)

    # Use Cohere LLM (model must be 'command')
    llm = Cohere(cohere_api_key=cohere_key, model="command")

    qa = RetrievalQA.from_chain_type(llm=llm, retriever=vectordb.as_retriever())

    result = qa.run(question)
    return result, "Answer generated using Cohere"
