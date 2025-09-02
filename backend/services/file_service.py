import PyPDF2
from fastapi import HTTPException
from io import BytesIO


def extract_text_from_pdf(file_content: bytes) -> str:
    try:
        pdf_reader = PyPDF2.PdfReader(BytesIO(file_content))
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"
        return text.strip()
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erro ao processar PDF: {str(e)}")


def extract_text_from_txt(file_content: bytes) -> str:
    try:
        return file_content.decode('utf-8')
    except UnicodeDecodeError:
        try:
            return file_content.decode('latin-1')
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Erro ao decodificar arquivo de texto: {str(e)}")


def validate_file_type(filename: str) -> str:
    if filename.lower().endswith('.pdf'):
        return 'pdf'
    elif filename.lower().endswith('.txt'):
        return 'txt'
    else:
        raise HTTPException(status_code=400, detail="Formato de arquivo não suportado. Use PDF ou TXT.")
