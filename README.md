# 🇮🇹 Tutor de Italiano IA

Um agente de IA completo para aprendizado de italiano, construído com LangChain e Gradio, oferecendo uma experiência educativa interativa, estruturada e personalizada.

## Visão Geral

O **Tutor de Italiano IA** é uma aplicação educativa avançada que utiliza inteligência artificial para ensinar italiano de forma interativa e personalizada. O projeto combina o poder do modelo Gemini do Google com uma interface web intuitiva criada em Gradio, oferecendo múltiplas funcionalidades educativas numa arquitetura modular e extensível.

### Propósito

Este projeto foi desenvolvido para:

- Fornecer um tutor de italiano disponível 24/7.
- Oferecer uma experiência de aprendizado estruturada com planos de estudo.
- Criar um ambiente seguro para a prática de conversação através de simulações (role-play).
- Disponibilizar recursos educativos diversificados numa única plataforma.
- Demonstrar a aplicação prática de LangChain e Gradio em projetos educacionais.

### Funcionalidades Principais

1. **Chat Inteligente com Memória**: Converse em italiano com um tutor que se lembra do contexto da conversa, oferece correções e explicações gramaticais.
2. **Plano de Estudos Estruturado**: Currículo completo do nível A1 ao C2, com lições detalhadas sobre gramática, vocabulário e exercícios.
3. **Simulação de Conversas (Role-play)**: Pratique cenários do dia a dia — por exemplo, pedir num café ou resolver um problema num hotel — interagindo com a IA.
4. **Tradução com Contexto**: Traduções entre português e italiano que vão além do literal, explicando expressões idiomáticas e nuances culturais.
5. **Quizzes Dinâmicos**: Quizzes interativos com perguntas de múltipla escolha e de preenchimento de lacunas.
6. **Recomendações Culturais**: Sugestões de filmes, séries, livros e músicas italianas, com nível de dificuldade e onde encontrar.
7. **Prática de Pronúncia (Text-to-Speech)**: Ouça a pronúncia correta de qualquer resposta do tutor com gTTS.

### Tecnologias Utilizadas

- **LangChain**: Framework para desenvolvimento de aplicações com LLMs.
- **Google Gemini**: Modelo de linguagem avançado via `langchain-google-genai`.
- **Gradio**: Interface web interativa e responsiva.
- **gTTS**: Biblioteca do Google para funcionalidade de Text-to-Speech.
- **Python**: Linguagem de programação principal.

## Requisitos de Sistema

### Pré-requisitos

- **Python 3.8+**: Versão mínima recomendada.
- **pip**: Gerenciador de pacotes Python.
- **Chave da API do Google**: Para acesso ao modelo Gemini.
- **Conexão com Internet**: Necessária para o modelo e integrações.

### Dependências Python

O arquivo `requirements.txt` contém todas as dependências necessárias:

```
langchain
langchain-google-genai
langchain-community
gradio
python-dotenv
beautifulsoup4
gTTS
```

### Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto com a sua chave da API do Google:

```env
GOOGLE_API_KEY=sua_chave_da_api_do_google_aqui
```

## Estrutura de Ficheiros

O projeto foi refatorado para uma arquitetura mais limpa e modular, especialmente na interface do utilizador.

```
tutor-italiano-ia/
├── main.py
├── requirements.txt
├── .env
├── test_basic_functionality.py
├── README.md
│
├── agents/
│   ├── gemini_model.py
│   ├── general_tutor_agent.py
│   ├── grammar_agent.py
│   ├── lessons_agent.py
│   ├── quiz_agent.py
│   ├── recommendation_agent.py
│   ├── roleplay_agent.py
│   ├── router_agent.py
│   └── translation_agent.py
│
├── core/
│   └── curriculum.py
│
├── prompts/
│   ├── general_tutor_prompts.py
│   ├── grammar_prompts.py
│   ├── lessons_prompts.py
│   ├── quiz_prompts.py
│   ├── recommendation_prompts.py
│   ├── roleplay_prompts.py
│   └── translation_prompts.py
│
└── ui/
    ├── tabs/
    │   ├── chat_tab.py
    │   ├── lesson_plan_tab.py
    │   ├── quick_tools_tab.py
    │   └── roleplay_tab.py
    ├── helpers.py
    ├── logic_handler.py
    ├── main_interface.py
    └── styles.py

```

### Descrição dos Componentes

#### `agents/`

Contém todos os agentes especializados do sistema:

- **`gemini_model.py`**: Configuração e inicialização do modelo Gemini.
- **`general_tutor_agent.py`**: Agente principal para conversação, correções e feedback.
- **`grammar_agent.py`**: Explicações e exercícios de gramática.
- **`lessons_agent.py`**: Geração de lições e planos de estudo.
- **`quiz_agent.py`**: Criação de quizzes dinâmicos.
- **`recommendation_agent.py`**: Sugestões culturais e conteúdo recomendado.
- **`roleplay_agent.py`**: Simulações e role-plays interativos.
- **`router_agent.py`**: Roteamento inteligente das mensagens entre agentes.
- **`translation_agent.py`**: Traduções com contexto entre português e italiano.

#### `core/`

- **`curriculum.py`**: Estrutura do currículo do A1 ao C2 e mapeamento de tópicos.

#### `prompts/`

Templates de prompts organizados por funcionalidade, permitindo fácil manutenção e personalização.

#### `ui/`

Interface do usuário construída com Gradio, oferecendo abas e componentes para cada modo de aprendizado.

##  Como Executar: Um Guia Detalhado

Para colocar o Tutor de Italiano IA em funcionamento, siga este guia passo a passo.

### 1. Clone ou Baixe o Projeto

- Com Git:
```bash
git clone <URL_DO_REPOSITORIO>
```
- Sem Git: baixe e descompacte o `.zip`.

### 2. Crie um Ambiente Virtual

```bash
python -m venv venv
```

Ative-o:

- Windows: `.\venv\Scripts\activate`
- Linux/macOS: `source venv/bin/activate`

### 3. Instale as Dependências

```bash
pip install -r requirements.txt
```

### 4. Configure as Variáveis de Ambiente

Crie ou edite o arquivo `.env` na pasta do projeto e adicione sua chave da API do Google:

```env
GOOGLE_API_KEY=your_google_api_key_here
```

### 5. Execute o Teste Básico (Opcional)

```bash
python test_basic_functionality.py
```

### 6. Inicie a Aplicação

```bash
python main.py
```

Após o carregamento, normalmente será exibida uma URL local, por exemplo: `http://127.0.0.1:7860`. Abra essa URL no navegador para acessar a interface do Tutor de Italiano IA.

## Como Usar

A interface oferece abas dedicadas para diferentes modos de aprendizado:

-  **Chat Inteligente**
  - Converse livremente com o tutor.
  - Peça explicações, traduções ou correções.
  - Clique em qualquer resposta do tutor para ouvir a pronúncia.

-  **Plano de Estudos**
  - Escolha o seu nível de proficiência (A1 a C2).
  - Selecione um tópico específico e receba uma lição completa.

- **Simulação (Role-play)**
  - Descreva um cenário que queira praticar.
  - A IA assume um papel e conduz a simulação.

-  **Ferramentas Rápidas**
  - Tradutor contextual.
  - Quizzes dinâmicos.
  - Recomendações culturais.

### Exemplos Rápidos

**Conversação**
```
Usuário: "Ciao! Come stai oggi?"
Agente: "Ciao! Sto bene, grazie! E tu come stai?"
```

**Tradução**
```
Usuário: "Traduza: Eu gosto muito de pizza italiana"
Agente: "Mi piace molto la pizza italiana"
```

**Quiz**
```
Usuário: "Quero um quiz sobre verbos"
Agente: "Qual é a conjugação correta do verbo 'essere' na primeira pessoa do singular?
a) sono  b) sei  c) è  d) siamo
Resposta correta: a) sono"
```

## Desenvolvimento e Extensão

### Adicionando Novos Agentes

1. Crie o arquivo do agente em `agents/`.
2. Defina o prompt em `prompts/`.
3. Atualize o `router_agent.py`.
4. Integre na interface Gradio em `ui/main_interface.py`.

### Personalizando Prompts

Edite os arquivos em `prompts/` e rode os testes para verificar o comportamento.

### Ferramentas Auxiliares

Você pode adicionar utilitários em uma pasta `tools/` e integrá-los aos agentes conforme necessário.

## Solução de Problemas Comuns

**Erro: "GOOGLE_API_KEY not found"**
- Verifique se o `.env` existe na raiz do projeto.
- Confirme se a variável `GOOGLE_API_KEY` está definida corretamente.
- Teste sua chave no Google AI Studio.

**Erro: "No module named 'langchain'"**
- Execute `pip install -r requirements.txt`.
- Verifique se está no ambiente virtual correto.

**Interface não carrega**
- Verifique se a porta 7860 não está em uso.
- Tente `http://localhost:7860` ou `http://127.0.0.1:7860`.

## Contribuição

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do projeto.
2. Crie uma branch para sua feature:
```bash
git checkout -b feature/nova-funcionalidade
```
3. Commit suas mudanças:
```bash
git commit -am "Adiciona nova funcionalidade"
```
4. Push para a branch:
```bash
git push origin feature/nova-funcionalidade
```
5. Abra um Pull Request.

## Suporte

Se encontrar problemas ou tiver dúvidas:

1. Verifique a seção de **Solução de Problemas**.
2. Execute o script de teste: `python test_basic_functionality.py`.
3. Consulte a documentação das dependências:
   - LangChain: https://python.langchain.com/
   - Gradio: https://gradio.app/
   - Google AI: https://ai.google.dev/

---

**Buona fortuna con il tuo apprendimento dell'italiano! 🇮🇹✨**
