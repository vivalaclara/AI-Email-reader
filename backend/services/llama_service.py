import os
import requests
from dotenv import load_dotenv

load_dotenv()


def call_llama4_maverick(prompt: str) -> dict:
    """
    Faz chamada para a API do Llama 4 Maverick via OpenRouter
    
    Args:
        prompt (str): Texto a ser enviado para o modelo
        
    Returns:
        dict: Resposta da API
        
    Raises:
        ValueError: Se a API key não estiver configurada
        requests.HTTPError: Se houver erro na requisição
    """
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
