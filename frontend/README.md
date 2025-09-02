# Frontend - AI Email Analyzer

Interface web construída com Next.js, TypeScript e Tailwind CSS para o sistema de análise de emails.

## Funcionalidades

- ✏️ **Entrada de texto**: Permite colar diretamente o conteúdo do email
- 📁 **Upload de arquivos**: Suporte para arquivos .txt e .pdf
- 🔄 **Processamento em tempo real**: Loading states e feedback visual
- 📊 **Visualização de resultados**: 
  - Classificação (Produtivo/Improdutivo)
  - Resposta sugerida
  - Conteúdo analisado
- 📋 **Funcionalidades extras**: Copiar resposta para área de transferência

## Estrutura dos Componentes

```
components/
├── FileUpload.tsx      # Upload com drag & drop
├── TextInput.tsx       # Formulário de entrada de texto
├── ResultDisplay.tsx   # Exibição dos resultados
└── LoadingSpinner.tsx  # Estado de carregamento

services/
└── emailService.ts     # Comunicação com API

types/
└── email.ts           # Tipos TypeScript
```

## Como usar

1. Acesse http://localhost:3000
2. Escolha entre inserir texto ou fazer upload de arquivo
3. Aguarde o processamento
4. Visualize a classificação e resposta sugerida

## Separação de Responsabilidades

- **FileUpload**: Gerencia upload e validação de arquivos
- **TextInput**: Formulário controlado para entrada de texto  
- **ResultDisplay**: Apresentação formatada dos resultados
- **LoadingSpinner**: Estados de loading reutilizável
- **EmailService**: Abstração da comunicação com API
- **Types**: Tipagem TypeScript para maior segurança
