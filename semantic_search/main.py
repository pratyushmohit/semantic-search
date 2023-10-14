import json
from io import StringIO

import pandas as pd
import uvicorn
from fastapi import File, Request, Response, UploadFile

from semantic_search.embedding_gen import SentenceEncoder
from semantic_search.vector_database import QdrantVectorDatabase

from . import app

COLLECTION_NAME = "test"

# ---- ENDPOINTS ----
@app.get("/status")
def status():
    output = json.dumps({"status": "Running"}, indent=4, default=str)
    return Response(content=output, media_type="application/json")


@app.post("/upload-file")
def upload_file(file: UploadFile = File(...)):
    contents = file.file.read()
    s = str(contents, 'utf-8')
    data = StringIO(s)
    df = pd.read_csv(data, sep=",", low_memory=False)
    df = df["review_text"]

    encoder = SentenceEncoder()
    embeddings = encoder.encode(df.tolist())
    embeddings = pd.DataFrame(embeddings)

    vector_database = QdrantVectorDatabase()
    vector_database.create_collection(
        collection_name=COLLECTION_NAME, embed_size=embeddings.shape[1])
    upsert_request = {"collection_name": COLLECTION_NAME,
                      "embeddings": embeddings}
    result = vector_database.upsert(upsert_request)

    if result["message"] == "Upsert successful":
        output = json.dumps(
            {"messaage": "Generated embeddings. Upsert Successful!"}, indent=4, default=str)

    return Response(content=output, media_type="application/json")


@app.get("/find-similar")
def find_similar(request: Request):
    sentence = request.query_params["sentence"]
    limit = request.query_params["limit"]
    encoder = SentenceEncoder()
    embeddings = encoder.encode(sentence).tolist()

    request = {"collection_name": COLLECTION_NAME,
               "embeddings": embeddings,
               "limit": limit}

    vector_database = QdrantVectorDatabase()
    output = vector_database.find_similar(request)
    output = json.dumps({"output": output},  indent=4, default=dict)
    return Response(content=output, media_type="application/json")


if __name__=="__main__":
    uvicorn.run("semantic_search.main:app", host="0.0.0.0", port=8000, reload=True)
