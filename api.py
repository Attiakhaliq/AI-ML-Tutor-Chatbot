from fastapi import FastAPI
from pydantic import BaseModel

from typing import List

from chatbot import Chatbot 

app = FastAPI(
    title= "AI & Machine Learning Model",
    description= "A conversioanl AI tutor for beginners."

)

bot = Chatbot()

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def home():
    return {"message": " AI machine learning Tutor API is running."}


@app.post("/chat")
def chat(request: ChatRequest):
    answer= bot.chat(request.message)
    return {"response": answer}


    