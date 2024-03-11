from pydantic import BaseModel
from fastapi import FastAPI
import hashlib
import base64
import os

class Text(BaseModel):
    text: str

app = FastAPI()

@app.post("/checksum")
def calculate_checksum(text: Text):
    checksum = hashlib.md5(text.text.encode()).hexdigest()
    return {"checksum": checksum}