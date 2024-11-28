
from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest

blob_url = ""

KEY = ""
ENDPOINT = ""

def credit_card_info(blob_url):
    credential = AzureKeyCredential(KEY)
    document_intelligence_client = DocumentIntelligenceClient(ENDPOINT, credential)

    card_info = document_intelligence_client.begin_analyze_document("prebuilt-creditCard", AnalyzeDocumentRequest(url_source=blob_url))

    print(card_info.result())

if __name__ == "__main__":
    credit_card_info(blob_url)