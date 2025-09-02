from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from models.email_models import (
    PromptRequest, 
    EmailProcessRequest, 
    EmailProcessResponse,
    EmailAnalysisResult
)


from services.llama_service import call_llama4_maverick
from services.file_service import extract_text_from_pdf, extract_text_from_txt, validate_file_type
from services.email_analysis_service import analyze_email_content
from services.security_service import validate_file_security
from services.logging_service import setup_logging, log_api_usage
import time
import os

load_dotenv()

logger, security_logger = setup_logging()
app = FastAPI(title="AI Email Analyzer", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        os.getenv("FRONTEND_URL", "http://localhost:3000"),
        "http://127.0.0.1:3000",
        "http://localhost:3001",
        "http://localhost:3000",
        "http://192.168.3.10:3000"  # Para acesso via rede local
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "AI Email Analyzer API", "status": "running"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "ai-email-analyzer"}

@app.post("/llama4")
async def llama4_endpoint(req: PromptRequest):
    resposta = call_llama4_maverick(req.prompt)
    return resposta

@app.post("/process-email-text", response_model=EmailProcessResponse)
async def process_email_text(req: EmailProcessRequest):
    start_time = time.time()
    
    try:
        analysis_result = analyze_email_content(req.text_content)
        analysis = EmailAnalysisResult(**analysis_result)
        
        processing_time = time.time() - start_time
        log_api_usage("/process-email-text", len(req.text_content), processing_time)
        
        return EmailProcessResponse(
            content=req.text_content,
            file_type="text",
            analysis=analysis
        )
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Erro ao processar email de texto: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro interno do servidor")
        raise

@app.post("/process-email-file", response_model=EmailProcessResponse)
async def process_email_file(file: UploadFile = File(...)):
    start_time = time.time()
    
    try:
        file_content = await file.read()
        
        validate_file_security(file.filename, len(file_content))
        
        file_type = validate_file_type(file.filename)
        
        if file_type == 'pdf':
            extracted_text = extract_text_from_pdf(file_content)
        else:
            extracted_text = extract_text_from_txt(file_content)
        
        if not extracted_text.strip():
            raise HTTPException(status_code=400, detail="Não foi possível extrair texto do arquivo.")
        
        analysis_result = analyze_email_content(extracted_text)
        analysis = EmailAnalysisResult(**analysis_result)
        
        processing_time = time.time() - start_time
        log_api_usage("/process-email-file", len(extracted_text), processing_time)
        
        return EmailProcessResponse(
            content=extracted_text,
            file_type=file_type,
            analysis=analysis
        )
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Erro ao processar arquivo: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro interno do servidor")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
