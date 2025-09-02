import { EmailProcessResponse, EmailProcessRequest } from '@/types/email';

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

export class EmailService {
  static async processEmailText(textContent: string): Promise<EmailProcessResponse> {
    try {
      console.log('Enviando requisição para:', `${API_BASE_URL}/process-email-text`);
      
      const response = await fetch(`${API_BASE_URL}/process-email-text`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text_content: textContent }),
      });

      console.log('Status da resposta:', response.status);
      
      if (!response.ok) {
        const errorText = await response.text();
        console.error('Erro na resposta:', errorText);
        throw new Error(`Erro ao processar texto: ${response.status} - ${errorText}`);
      }

      const result = await response.json();
      console.log('Resultado recebido:', result);
      return result;
    } catch (error) {
      console.error('Erro na requisição:', error);
      throw error;
    }
  }

  static async processEmailFile(file: File): Promise<EmailProcessResponse> {
    try {
      console.log('Enviando arquivo para:', `${API_BASE_URL}/process-email-file`);
      
      const formData = new FormData();
      formData.append('file', file);

      const response = await fetch(`${API_BASE_URL}/process-email-file`, {
        method: 'POST',
        body: formData,
      });

      console.log('Status da resposta:', response.status);

      if (!response.ok) {
        const errorText = await response.text();
        console.error('Erro na resposta:', errorText);
        throw new Error(`Erro ao processar arquivo: ${response.status} - ${errorText}`);
      }

      const result = await response.json();
      console.log('Resultado recebido:', result);
      return result;
    } catch (error) {
      console.error('Erro na requisição:', error);
      throw error;
    }
  }
}
