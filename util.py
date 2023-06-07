import os  
import openai 
from dotenv import load_dotenv

load_dotenv() 
openai.api_type = "azure"  
openai.api_key = os.getenv("OPENAI_API_KEY")  
openai.api_base = os.getenv("OPENAI_ENDPOINT")  
openai.api_version = os.getenv("OPENAI_API_VERSION")  


def generate_embeddings(text, model="text-embedding-ada-002"):
    response = openai.Embedding.create(
        input=text, engine=model)
    embeddings = response['data'][0]['embedding']
    return embeddings