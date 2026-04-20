from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Msg(BaseModel):
    text: str

@app.get("/")
def home():
    return {"status":"running"}

@app.post("/chat")
def chat(data: Msg):
    return {"reply": "Hello " + data.text}