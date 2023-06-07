import os  
import json  
from dotenv import load_dotenv
from azure.core.credentials import AzureKeyCredential  
from azure.search.documents import SearchClient, IndexDocumentsBatch  
from azure.search.documents.indexes import SearchIndexClient  
from azure.search.documents.models import Vector 
import util


load_dotenv()
service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")  
index_name = os.getenv("AZURE_SEARCH_INDEX_NAME")  
key = os.getenv("AZURE_SEARCH_ADMIN_KEY")  
credential = AzureKeyCredential(key)
deployed_model = os.getenv("OPENAI_EMBEDDING_DEPLOYED_MODEL")

query = "What services are best for asynchronous communication?" 
#query = "¿Qué servicios son los mejores para la comunicación asíncrona?" # In Spanish

search_client = SearchClient(endpoint=service_endpoint, index_name=index_name, credential=credential)

results = search_client.search(  
    search_text=query, 
    vector=Vector(value=util.generate_embeddings(query, deployed_model), k=4, fields="contentVector"),  
    select=["title", "content", "category"],
    top=4
)  

#d= [result for result in results]
#print(json.dumps(d))

for result in results:  
    print(f"Score: {result['@search.score']}") 
    print(f"Title: {result['title']}")  
    print(f"Content: {result['content']}")  
    print(f"Category: {result['category']}\n") 