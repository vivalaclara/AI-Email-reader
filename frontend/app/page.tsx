'use client';

import { useState } from 'react';
import { PencilSimple, FolderOpen } from '@phosphor-icons/react';
import FileUpload from '@/components/FileUpload';
import TextInput from '@/components/TextInput';
import ResultDisplay from '@/components/ResultDisplay';
import LoadingSpinner from '@/components/LoadingSpinner';
import { EmailService } from '@/services/emailService';
import { EmailProcessResponse } from '@/types/email';

export default function Home() {
  const [result, setResult] = useState<EmailProcessResponse | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [activeTab, setActiveTab] = useState<'text' | 'file'>('text');

  const handleTextSubmit = async (text: string) => {
    setLoading(true);
    setError(null);
    
    try {
      const response = await EmailService.processEmailText(text);
      setResult(response);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Erro desconhecido');
    } finally {
      setLoading(false);
    }
  };

  const handleFileSelect = async (file: File) => {
    setLoading(true);
    setError(null);
    
    try {
      const response = await EmailService.processEmailFile(file);
      setResult(response);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Erro desconhecido');
    } finally {
      setLoading(false);
    }
  };

  const handleReset = () => {
    setResult(null);
    setError(null);
  };

  if (result) {
    return (
      <div className="min-h-screen bg-gray-50 p-4">
        <div className="container mx-auto py-8">
          <ResultDisplay result={result} onReset={handleReset} />
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-50 p-4">
      <div className="container mx-auto max-w-4xl py-8">
        {/* Header */}
        <div className="text-center mb-8">
          <h1 className="text-4xl font-bold text-gray-800 mb-4">
            Email Analyzer
          </h1>
          <p className="text-lg text-gray-600">
            Classifique emails automaticamente e receba sugestões de resposta
          </p>
        </div>

        {/* Error Message */}
        {error && (
          <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-6">
            <strong>Erro:</strong> {error}
          </div>
        )}

        {/* Loading */}
        {loading && (
          <div className="bg-white rounded-lg shadow-md p-8 mb-6">
            <LoadingSpinner message="Analisando email..." />
          </div>
        )}

        {/* Main Content */}
        {!loading && (
          <div className="bg-white rounded-lg shadow-md p-6">
            {/* Tabs */}
            <div className="flex border-b border-gray-200 mb-6">
              <button
                className={`py-2 px-4 font-medium text-sm flex items-center gap-2 ${
                  activeTab === 'text'
                    ? 'border-b-2 border-blue-500 text-blue-600'
                    : 'text-gray-500 hover:text-gray-700'
                }`}
                onClick={() => setActiveTab('text')}
              >
                <PencilSimple size={16} />
                Inserir Texto
              </button>
              <button
                className={`py-2 px-4 font-medium text-sm flex items-center gap-2 ${
                  activeTab === 'file'
                    ? 'border-b-2 border-blue-500 text-blue-600'
                    : 'text-gray-500 hover:text-gray-700'
                }`}
                onClick={() => setActiveTab('file')}
              >
                <FolderOpen size={16} />
                Upload de Arquivo
              </button>
            </div>

            {/* Tab Content */}
            {activeTab === 'text' && (
              <TextInput onTextSubmit={handleTextSubmit} disabled={loading} />
            )}

            {activeTab === 'file' && (
              <FileUpload onFileSelect={handleFileSelect} disabled={loading} />
            )}
          </div>
        )}

        {/* Footer */}
        <div className="text-center mt-8 text-sm text-gray-500">
          <p>Sistema de Análise de Emails • FastAPI • Next.js</p>
        </div>
      </div>
    </div>
  );
}
