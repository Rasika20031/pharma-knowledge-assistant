import chromadb

client = chromadb.PersistentClient(path="./chroma_storage")

collection = client.get_or_create_collection(
    name="pharma_documents"
)

def get_collection():
    return collection
