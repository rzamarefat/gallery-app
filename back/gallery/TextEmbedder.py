import openai
from langchain.embeddings import OpenAIEmbeddings
from dotenv import find_dotenv, load_dotenv
import os

load_dotenv(find_dotenv())
openai.api_key = os.getenv("OPENAI_API_KEY")

class TextEmbedder:
    def __init__(self):
        self._embeddings_model = OpenAIEmbeddings()

    def __call__(self, text):
        
        embedding = self._embeddings_model.embed_query(text)

        return embedding