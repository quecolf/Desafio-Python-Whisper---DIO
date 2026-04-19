# 🎙️ Audio Summarizer Agent

Um agente simples que grava áudio, transcreve automaticamente e gera um resumo usando IA.

## 🚀 Funcionalidades

- 🎤 Grava áudio diretamente do navegador (Google Colab)
- 🧾 Transcreve o áudio com Whisper
- 🧠 Resume o conteúdo utilizando modelos da OpenAI
- ⚡ Pipeline completo: áudio → texto → resumo

---

## 🧠 Como funciona

O projeto segue o fluxo:

1. Gravação de áudio  
2. Transcrição com Whisper  
3. Processamento com IA (resumo)  
4. Exibição do resultado  

---

## 📁 Estrutura do projeto
audio-agent/
│
├── main.py
├── recorder.py
├── transcriber.py
├── summarizer.py
├── requirements.txt
└── README.md

---

## ⚙️ Instalação

Clone o repositório:

git clone https://github.com/seu-usuario/audio-agent.git
cd audio-agent

Instale os itens em requirements.txt

## 🔑 Configuração da API

Este projeto utiliza a API da OpenAI para gerar os resumos.

Você precisa criar uma chave em:
https://platform.openai.com/api-keys

Depois, configure a variável de ambiente:

Linux / Mac:
export OPENAI_API_KEY="sua_chave_aqui"
Windows:
setx OPENAI_API_KEY "sua_chave_aqui"

## ▶️ Como usar

Execute o arquivo principal:

python main.py

O programa irá:

1. Gravar um áudio
2. Transcrever automaticamente
3. Gerar um resumo do conteúdo

## ⚠️ Observações
Sem uma API Key válida, o resumo não será gerado
O projeto pode rodar em modo "demo" caso a chave não esteja configurada
O Whisper roda localmente, então pode consumir mais recursos dependendo do modelo

