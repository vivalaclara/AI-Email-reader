from pydantic import BaseModel
from typing import Optional


class EmailResponse(BaseModel):
    category: str
    suggestion: str


class PromptRequest(BaseModel):
    prompt: str


class EmailProcessRequest(BaseModel):
    text_content: str


class EmailAnalysisResult(BaseModel):
    categoria: str
    confianca: int
    resumo: str
    motivo: str
    sugestao_resposta: Optional[str] = None
    raw_response: Optional[str] = None


class EmailProcessResponse(BaseModel):
    content: str
    file_type: str
    analysis: EmailAnalysisResult
