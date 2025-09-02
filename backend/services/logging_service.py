import logging
import os
from datetime import datetime

# Configuração de logging
def setup_logging():
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    logger = logging.getLogger("ai_emails")
    logger.setLevel(logging.INFO)
    
    file_handler = logging.FileHandler(f"{log_dir}/ai_emails.log")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    security_logger = logging.getLogger("security")
    security_logger.setLevel(logging.WARNING)
    
    security_handler = logging.FileHandler(f"{log_dir}/security.log")
    security_handler.setFormatter(formatter)
    security_logger.addHandler(security_handler)
    
    return logger, security_logger

def log_security_event(event_type: str, details: str, severity: str = "WARNING"):
    security_logger = logging.getLogger("security")
    
    log_message = f"{event_type}: {details}"
    
    if severity == "INFO":
        security_logger.info(log_message)
    elif severity == "WARNING":
        security_logger.warning(log_message)
    elif severity == "ERROR":
        security_logger.error(log_message)
    elif severity == "CRITICAL":
        security_logger.critical(log_message)

def log_api_usage(endpoint: str, content_length: int, processing_time: float):
    logger = logging.getLogger("ai_emails")
    logger.info(f"API_USAGE - Endpoint: {endpoint}, Content Length: {content_length}, Time: {processing_time:.2f}s")
