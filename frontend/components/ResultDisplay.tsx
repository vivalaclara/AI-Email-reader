'use client';

import { EmailProcessResponse } from '@/types/email';
import { ChartBar, ChatCircle, File, Copy } from '@phosphor-icons/react';

interface ResultDisplayProps {
  result: EmailProcessResponse;
  onReset: () => void;
}

export default function ResultDisplay({ result, onReset }: ResultDisplayProps) {
  const isProductive = result.analysis.categoria === 'Produtivo';

  return (
    <div className="w-full max-w-4xl mx-auto space-y-6">
      {/* Cabeçalho */}
      <div className="flex justify-between items-center">
        <h2 className="text-2xl font-bold text-gray-800">Resultado da Análise</h2>
        <button
          onClick={onReset}
          className="px-4 py-2 bg-gray-500 text-white rounded-md hover:bg-gray-600 transition-colors"
        >
          Nova Análise
        </button>
      </div>

      {/* Classificação */}
      <div className="bg-white p-6 rounded-lg shadow-md border-l-4 border-l-blue-500">
        <h3 className="text-lg font-semibold text-gray-800 mb-3 flex items-center gap-2">
          <ChartBar size={20} />
          Classificação
        </h3>
        <div className={`inline-flex px-4 py-2 rounded-full text-sm font-medium ${
          isProductive 
            ? 'bg-green-100 text-green-800' 
            : 'bg-yellow-100 text-yellow-800'
        }`}>
          {result.analysis.categoria}
        </div>
        {result.analysis.confianca && (
          <p className="text-sm text-gray-600 mt-2">
            Confiança: {result.analysis.confianca}%
          </p>
        )}
        {result.analysis.resumo && (
          <p className="text-sm text-gray-700 mt-2">
            <strong>Resumo:</strong> {result.analysis.resumo}
          </p>
        )}
        {result.analysis.motivo && (
          <p className="text-sm text-gray-700 mt-2">
            <strong>Motivo:</strong> {result.analysis.motivo}
          </p>
        )}
      </div>

      {/* Resposta Sugerida */}
      <div className="bg-white p-6 rounded-lg shadow-md border-l-4 border-l-green-500">
        <h3 className="text-lg font-semibold text-gray-800 mb-3 flex items-center gap-2">
          <ChatCircle size={20} />
          Resposta Sugerida
        </h3>
        {result.analysis.sugestao_resposta ? (
          <div>
            <div className="bg-gray-50 p-4 rounded-md">
              <p className="text-gray-700 whitespace-pre-wrap">{result.analysis.sugestao_resposta}</p>
            </div>
            <button
              onClick={() => navigator.clipboard.writeText(result.analysis.sugestao_resposta!)}
              className="mt-3 px-3 py-1 bg-blue-500 text-white text-sm rounded hover:bg-blue-600 transition-colors flex items-center gap-1"
            >
              <Copy size={14} />
              Copiar Resposta
            </button>
          </div>
        ) : (
          <div className="bg-gray-50 p-4 rounded-md">
            <p className="text-gray-500 italic">
              Nenhuma resposta específica necessária para este tipo de email.
            </p>
          </div>
        )}
      </div>

      {/* Conteúdo Analisado */}
      <div className="bg-white p-6 rounded-lg shadow-md border-l-4 border-l-gray-500">
        <h3 className="text-lg font-semibold text-gray-800 mb-3 flex items-center gap-2">
          <File size={20} />
          Conteúdo Analisado
        </h3>
        <div className="bg-gray-50 p-4 rounded-md max-h-60 overflow-y-auto">
          <p className="text-gray-700 text-sm whitespace-pre-wrap">{result.content}</p>
        </div>
        <p className="text-xs text-gray-500 mt-2">
          Tipo de arquivo: {result.file_type}
        </p>
      </div>
    </div>
  );
}
