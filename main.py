# Backend: FastAPI (main.py)
from fastapi import FastAPI
from pydantic import BaseModel
import openai
import os

app = FastAPI()

# Load API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

class LetterRequest(BaseModel):
    theme: str
    recipient: str
    sender: str

@app.post("/generate-letter")
def generate_letter(request: LetterRequest):
    prompt = f"Write a lost letter with the theme '{request.theme}', from {request.sender} to {request.recipient}."
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are a poetic and historical letter writer."},
                  {"role": "user", "content": prompt}]
    )
    return {"letter": response["choices"][0]["message"]["content"]}

# Run with: uvicorn main:app --host 0.0.0.0 --port 8000

