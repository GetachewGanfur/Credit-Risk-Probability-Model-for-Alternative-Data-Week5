from fastapi import FastAPI
from . import pydantic_models

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Credit Risk Model API"} 