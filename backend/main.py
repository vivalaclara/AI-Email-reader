from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import os
import requests
load_dotenv()


class EmailResponse(BaseModel):
    category: str
    suggestion: str

class PromptRequest(BaseModel):
    prompt: str

app = FastAPI()


def call_llama4_maverick(prompt):
    api_key = os.getenv('OPENROUTER_API_KEY')
    if not api_key:
        raise ValueError('API key não encontrada. Defina OPENROUTER_API_KEY nas variáveis de ambiente.')
    url = 'https://openrouter.ai/api/v1/chat/completions'
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json',
        'HTTP-Referer': 'http://localhost',  
        'X-Title': 'AI-EMAILS'
    }
    data = {
        "model": "meta-llama/llama-4-maverick:free",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    return response.json()

@app.post("/llama4")
async def llama4_endpoint(req: PromptRequest):
    resposta = call_llama4_maverick(req.prompt)
    return resposta

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
