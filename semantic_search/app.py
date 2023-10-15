import ast
import json
from io import StringIO

import pandas as pd
from celery import Celery
from fastapi import File, Request, Response, UploadFile

from semantic_search.embedding_gen import SentenceEncoder
from semantic_search.vector_database import QdrantVectorDatabase

from . import app

celery = Celery(__name__, broker='redis://redis:6379/0',
                backend='redis://redis:6379/0')

# Use Redis as the backend
celery.conf.update(
    result_backend='redis://redis:6379/0',
    result_persistent=True,
)

COLLECTION_NAME = "test"

# ---- ENDPOINTS ----


@app.get("/status")
def status():
    output = json.dumps({"status": "Running"}, indent=4, default=str)
    return Response(content=output, media_type="application/json")


@celery.task
def generate_embeddings_and_upsert(contents):
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
            {"message": "Generated embeddings. Upsert Successful!"}, indent=4, default=str)
    return output


@app.post("/upload-file")
def upload_file(file: UploadFile = File(...)):
    contents = file.file.read()
    result = generate_embeddings_and_upsert.delay(contents)
    output = json.dumps({"message": "Process job created. Please check status in sometime!",
                        "task_id": result.id}, indent=4, default=str)

    return Response(content=output, media_type="application/json")


@app.get("/check-status/{task_id}")
async def check_status(task_id: str):
    result = generate_embeddings_and_upsert.AsyncResult(task_id, app=celery)

    if result.ready():
        if result.successful():
            result_data = result.result
            result_data = ast.literal_eval(result_data)
            return {"status": "completed", "result": result_data}
        else:
            return {"status": "failed", "result": None}
    else:
        return {"status": "pending", "result": None}


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
