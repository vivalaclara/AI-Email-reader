import re
from typing import List
from fastapi import HTTPException
from .logging_service import log_security_event

class SecurityConfig:
    MAX_CONTENT_LENGTH = 50000
    
    SUSPICIOUS_PATTERNS = [
        r'<script[^>]*>.*?</script>',
        r'javascript:',
        r'data:text/html',
        r'vbscript:',
    ]
    
    ALLOWED_EXTENSIONS = ['.pdf', '.txt']
    MAX_FILE_SIZE = 10 * 1024 * 1024

def validate_content_security(content: str) -> bool:
    if len(content) > SecurityConfig.MAX_CONTENT_LENGTH:
        log_security_event(
            "CONTENT_TOO_LARGE", 
            f"Conteúdo com {len(content)} caracteres excede limite de {SecurityConfig.MAX_CONTENT_LENGTH}",
            "WARNING"
        )
        raise HTTPException(
            status_code=413, 
            detail=f"Conteúdo muito longo. Máximo permitido: {SecurityConfig.MAX_CONTENT_LENGTH} caracteres"
        )
    
    for pattern in SecurityConfig.SUSPICIOUS_PATTERNS:
        if re.search(pattern, content, re.IGNORECASE):
            log_security_event(
                "SUSPICIOUS_CONTENT_DETECTED", 
                f"Padrão suspeito encontrado: {pattern}",
                "ERROR"
            )
            raise HTTPException(
                status_code=400, 
                detail="Conteúdo contém elementos potencialmente maliciosos"
            )
    
    return True

def validate_file_security(filename: str, file_size: int) -> bool:
    if not any(filename.lower().endswith(ext) for ext in SecurityConfig.ALLOWED_EXTENSIONS):
        raise HTTPException(
            status_code=400, 
            detail=f"Extensão não permitida. Extensões aceitas: {', '.join(SecurityConfig.ALLOWED_EXTENSIONS)}"
        )
    
    if file_size > SecurityConfig.MAX_FILE_SIZE:
        raise HTTPException(
            status_code=413, 
            detail=f"Arquivo muito grande. Tamanho máximo: {SecurityConfig.MAX_FILE_SIZE / (1024*1024):.1f}MB"
        )
    
    return True

def sanitize_content(content: str) -> str:
    content = re.sub(r'<[^>]+>', '', content)
    content = re.sub(r'[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]', '', content)
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    return content.strip()

def rate_limit_check(user_id: str = "default") -> bool:
    return True
