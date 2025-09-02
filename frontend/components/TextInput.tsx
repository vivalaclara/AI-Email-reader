'use client';

import { useState } from 'react';

interface TextInputProps {
  onTextSubmit: (text: string) => void;
  disabled?: boolean;
}

export default function TextInput({ onTextSubmit, disabled }: TextInputProps) {
  const [text, setText] = useState('');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (text.trim() && !disabled) {
      onTextSubmit(text.trim());
    }
  };

  return (
    <div className="w-full">
      <form onSubmit={handleSubmit} className="space-y-4">
        <div>
          <label htmlFor="email-text" className="block text-sm font-medium text-gray-700 mb-2">
            Conteúdo do Email
          </label>
          <textarea
            id="email-text"
            value={text}
            onChange={(e) => setText(e.target.value)}
            disabled={disabled}
            placeholder="Cole aqui o conteúdo do email que deseja analisar..."
            className="w-full h-40 p-3 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-blue-500 text-gray-900 placeholder-gray-500"
            required
          />
        </div>
        <button
          type="submit"
          disabled={!text.trim() || disabled}
          className="w-full py-2 px-4 bg-blue-600 text-white rounded-md hover:bg-blue-700 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
        >
          {disabled ? 'Processando...' : 'Analisar Email'}
        </button>
      </form>
    </div>
  );
}
