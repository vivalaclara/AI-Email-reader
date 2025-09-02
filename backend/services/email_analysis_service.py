from .llama_service import call_llama4_maverick
from .security_service import validate_content_security, sanitize_content
import json

def create_email_analysis_prompt(content: str) -> str:
    return f"""
Analise o seguinte conteúdo de email e forneça uma resposta em formato JSON seguindo exatamente esta estrutura:

{{
    "categoria": "Produtivo" ou "Improdutivo",
    "confianca": número de 0 a 100,
    "resumo": "resumo breve do conteúdo",
    "motivo": "explicação da classificação",
    "sugestao_resposta": "sugestão de resposta se aplicável ou null"
}}

**Critérios de classificação:**

**PRODUTIVO:** Emails que requerem uma ação ou resposta específica:
- Solicitações de suporte técnico
- Dúvidas sobre produtos/serviços
- Pedidos de informações
- Agendamento de reuniões
- Reclamações que precisam ser resolvidas
- Propostas comerciais
- Solicitações de orçamento
- Relatórios de problemas/bugs
- Atualizações sobre casos em aberto
- Pedidos de aprovação

**IMPRODUTIVO:** Emails que não necessitam de uma ação imediata:
- Mensagens de felicitações
- Agradecimentos simples
- Newsletters/boletins informativos
- Convites para eventos (sem resposta obrigatória)
- Comunicados gerais
- Spam/marketing não solicitado
- Mensagens automáticas de confirmação
- Notificações de sistema sem ação requerida

Conteúdo do email:
{content}

Responda APENAS com o JSON válido, sem texto adicional.
"""

def analyze_email_content(content: str) -> dict:
    validate_content_security(content)
    sanitized_content = sanitize_content(content)
    
    prompt = create_email_analysis_prompt(sanitized_content)
    
    try:
        response = call_llama4_maverick(prompt)
        llama_response = response['choices'][0]['message']['content']
        
        # Tenta extrair JSON da resposta
        try:
            start_idx = llama_response.find('{')
            end_idx = llama_response.rfind('}') + 1
            
            if start_idx != -1 and end_idx != 0:
                json_str = llama_response[start_idx:end_idx]
                analysis_result = json.loads(json_str)
                
                required_fields = ['categoria', 'confianca', 'resumo', 'motivo']
                if all(field in analysis_result for field in required_fields):
                    return analysis_result
                else:
                    raise ValueError("Campos obrigatórios ausentes na resposta")
            else:
                raise ValueError("JSON não encontrado na resposta")
                
        except (json.JSONDecodeError, ValueError) as e:
            return {
                "categoria": "Produtivo" if any(keyword in content.lower() for keyword in 
                    ["solicito", "preciso", "dúvida", "problema", "ajuda", "suporte", "urgente"]) else "Improdutivo",
                "confianca": 60,
                "resumo": content[:100] + "..." if len(content) > 100 else content,
                "motivo": "Análise automática - falha na estruturação da resposta do modelo",
                "sugestao_resposta": None,
                "raw_response": llama_response
            }
            
    except Exception as e:
        return {
            "categoria": "Improdutivo",
            "confianca": 30,
            "resumo": "Erro na análise",
            "motivo": f"Erro ao processar: {str(e)}",
            "sugestao_resposta": None
        }
