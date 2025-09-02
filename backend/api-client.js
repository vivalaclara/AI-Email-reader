const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

class EmailAnalyzerAPI {
  
  async healthCheck() {
    try {
      const response = await fetch(`${API_BASE_URL}/health`);
      return await response.json();
    } catch (error) {
      console.error('Erro ao verificar saúde da API:', error);
      throw error;
    }
  }

  async analyzeEmailText(text) {
    try {
      const response = await fetch(`${API_BASE_URL}/process-email-text`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          text_content: text
        })
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || 'Erro ao analisar email');
      }

      return await response.json();
    } catch (error) {
      console.error('Erro ao analisar texto do email:', error);
      throw error;
    }
  }

  async analyzeEmailFile(file) {
    try {
      const formData = new FormData();
      formData.append('file', file);

      const response = await fetch(`${API_BASE_URL}/process-email-file`, {
        method: 'POST',
        body: formData
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || 'Erro ao analisar arquivo');
      }

      return await response.json();
    } catch (error) {
      console.error('Erro ao analisar arquivo:', error);
      throw error;
    }
  }

  async callLlama(prompt) {
    try {
      const response = await fetch(`${API_BASE_URL}/llama4`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          prompt: prompt
        })
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || 'Erro ao chamar Llama');
      }

      return await response.json();
    } catch (error) {
      console.error('Erro ao chamar Llama:', error);
      throw error;
    }
  }
}

const emailAnalyzerAPI = new EmailAnalyzerAPI();

export default emailAnalyzerAPI;
