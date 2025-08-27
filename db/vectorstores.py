import chromadb
import uuid

client = chromadb.Client()

collection = client.create_collection(name="exam_info")

def vector_db():
    with open("exams.txt", "r", encoding="utf-8") as text:
        content = text.read().splitlines()

    collection.upsert(
        ids=[str(uuid.uuid4()) for _ in content],
        documents=content, 
        metadatas=[{"line": line} for line in range(len(content))]
    )

    print(collection.peek())

