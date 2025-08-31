from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import os
# from llama_cpp import Llama  
load_dotenv()

class EmailRequest(BaseModel):
    text: str

class EmailResponse(BaseModel):
    category: str
    suggestion: str

app = FastAPI()

@app.post("/classify", response_model=EmailResponse)
async def classify_email(req: EmailRequest):
    category = "Produtivo"
    suggestion = "Obrigado pelo seu contato, estamos analisando sua solicitação."
    return EmailResponse(category=category, suggestion=suggestion)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
