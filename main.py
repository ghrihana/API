from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Question(BaseModel):
    user_id: str
    question: str

@app.post("/ask")
async def ask_question(question: Question):
    # فرضاً اینجا محاسبات یا پردازش سؤال انجام می‌شود
    result = f"پاسخ به سؤال کاربر {question.user_id}: {question.question.upper()}"
    return {"result": result}