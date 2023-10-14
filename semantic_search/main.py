import json
from io import StringIO

import pandas as pd
from fastapi import File, Response, UploadFile

from semantic_search.embedding_gen import SentenceEncoder

from . import app


#---- ENDPOINTS ----
@app.get("/status")
def status():
    output = json.dumps({"status": "Running"}, indent=4, default=str)
    return Response(content=output, media_type="application/json")

@app.post("/upload-file")
def upload_file(file: UploadFile = File(...)):
    contents = file.file.read()
    s = str(contents,'utf-8')
    data = StringIO(s) 
    df = pd.read_csv(data, sep=",", low_memory=False)
    df = df["review_text"]
    print(df)

    encoder = SentenceEncoder()
    output = encoder.encode(list[df])

    return output

@app.post("/recommend")
def recommend(request):
    pass
