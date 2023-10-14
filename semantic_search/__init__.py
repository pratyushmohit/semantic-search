from fastapi import FastAPI

app = FastAPI(title="Semantic Search",
              description="Text search using vector databases.",
              version="0.1.0")