import os

from qdrant_client import QdrantClient
from qdrant_client.http import models
from qdrant_client.http.exceptions import UnexpectedResponse

QDRANT_HOST = os.environ.get("QDRANT_HOST", "localhost")
QDRANT_PORT = os.environ.get("QDRANT_PORT", 6333)

client = QdrantClient(host=QDRANT_HOST, port=QDRANT_PORT)


class QdrantVectorDatabase:
    def __init__(self) -> None:
        pass

    def create_collection(self, collection_name: str, embed_size: int):
        try:
            client.create_collection(
                collection_name=collection_name,
                vectors_config=models.VectorParams(
                    size=embed_size, distance=models.Distance.COSINE),
            )
        except UnexpectedResponse as e:
            error_message = "Collection `{}` already exists!".format(
                collection_name)
            if error_message in str(e):
                return {"error": "Collection already exists"}
            else:
                # To handle other cases of UnexpectedResponse if needed
                return {"error": "An unexpected error occurred"}

        return {"message": "Collection created successfully"}

    def upsert(self, request):
        if type(request) != dict:
            request = request.dict()
        collection_name = request["collection_name"]
        embeddings = request["embeddings"]
        # metadata = request["metadata"]

        client.upsert(collection_name=collection_name,
                      points=models.Batch(ids=list(embeddings.index),
                                          # payloads=metadata.to_dict("records"),
                                          vectors=embeddings.values.tolist())
                      )

        return {"message": "Upsert successful"}

    def find_similar(self, request):

        output = client.search(
            collection_name=request["collection_name"],
            query_vector=request["embeddings"],
            limit=request["limit"]
        )
        return output
