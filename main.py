import requests 
import uuid
from docx import Document

subscription_key = ""
url = "https://api.cognitive.microsofttranslator.com"
location = "eastus2"
target_language = "pt-br"
url_path = "/translate"
file_path = ""

complete_url = url + url_path

def translate_document(document_text):
    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        # location required if you're using a multi-service or regional (not global) resource.
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    body = [{ "text" : document_text }]

    params = {
        'api-version': '3.0',
        'from': 'en',
        'to': target_language
    }
    
    request = requests.post(complete_url, params=params, headers=headers, json=body)
    response = request.json()
    
    print(response)

if __name__ == "__main__":

    document = Document(file_path)

    fulltext = [paragraph for paragraph in document.paragraphs]

    translate_document(fulltext)

