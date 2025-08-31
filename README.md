# AI-EMAILS

Solução para classificar automaticamente emails em **Produtivo** ou **Improdutivo** e sugerir respostas automáticas, usando IA (Meta Llama 4 Maverick) no backend (FastAPI) e interface web em Next.js com Tailwind CSS.

## Estrutura do Projeto

```
AI-EMAILS/
├─ backend/    # FastAPI + Llama 4 Maverick
└─ frontend/   # Next.js + TypeScript + Tailwind CSS
```

## Como Baixar e Executar Localmente

1. Clone o repositório:

   ```bash
   git clone https://github.com/vivalaclara/AI-Email-reader
   cd AI-EMAILS
   ```

2. Configurar o Backend:

   ```bash
   cd backend
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   # Atualize o arquivo .env com o caminho do modelo Llama 4 Maverick
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

3. Configurar o Frontend:

   ```bash
   cd ../frontend
   npm install
   npm run dev
   ```

4. Acesse:

   - Frontend: http://localhost:3000
   - API docs (Swagger): http://localhost:8000/docs

## Como Subir para o GitHub

1. Inicialize o repositório local (caso ainda não tenha feito):

   ```bash
   cd /caminho/para/AI-EMAILS
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   ```

2. Adicione a origem remota e envie as alterações:

   ```bash
   git remote add origin https://github.com/SEU_USUARIO/AI-EMAILS.git
   git push -u origin main
   ```

> **Obs:** O `.gitignore` já exclui `node_modules/`, `backend/venv/`, `.env` e artefatos de build.
