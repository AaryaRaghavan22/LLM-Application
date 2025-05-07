# app.py

from fastapi import FastAPI
from pydantic import BaseModel
from your_pipeline import ask_question
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QuestionRequest(BaseModel):
    question: str

@app.post("/ask")
async def ask(request: QuestionRequest):
    user_question = request.question
    answer = ask_question(user_question)
    return {"answer": answer}