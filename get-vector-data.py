import os
import json 
import util 
from dotenv import load_dotenv

load_dotenv() 
deployed_model = os.getenv("OPENAI_EMBEDDING_DEPLOYED_MODEL")

with open('data/text-sample.json', 'r', encoding='utf-8') as file:
    input_data = json.load(file)

for item in input_data:
    title = item['title']
    content = item['content']
    title_embeddings = util.generate_embeddings(title, deployed_model)
    content_embeddings = util.generate_embeddings(content, deployed_model)
    item['titleVector'] = title_embeddings
    item['contentVector'] = content_embeddings
    item['@search.action'] = 'mergeOrUpload'

with open("data/docVectors.json", "w") as f:
    json.dump(input_data, f)