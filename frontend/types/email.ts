export interface EmailAnalysisResult {
  categoria: 'Produtivo' | 'Improdutivo';
  sugestao_resposta: string | null;
  confianca?: number;
  resumo?: string;
  motivo?: string;
}

export interface EmailProcessResponse {
  content: string;
  file_type: string;
  analysis: EmailAnalysisResult;
}

export interface EmailProcessRequest {
  text_content: string;
}
