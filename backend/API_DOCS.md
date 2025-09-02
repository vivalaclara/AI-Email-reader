# API - AI Email Analyzer

Base URL: `http://localhost:8000`

## Endpoints

### Health Check
`GET /health`

### Analisar Texto
`POST /process-email-text`
```json
{
  "text_content": "string"
}
```

### Analisar Arquivo
`POST /process-email-file`
FormData com arquivo PDF ou TXT

### Prompt Direto
`POST /llama4`
```json
{
  "prompt": "string"
}
```

## Response
```json
{
  "content": "string",
  "file_type": "text|pdf|txt",
  "analysis": {
    "categoria": "Produtivo|Improdutivo",
    "confianca": 85,
    "resumo": "string",
    "motivo": "string",
    "sugestao_resposta": "string|null"
  }
}
```

## Frontend Setup
```bash
NEXT_PUBLIC_API_URL=http://localhost:8000
```
