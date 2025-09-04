# 🇮🇹 Tutor de Italiano IA

Um agente de IA completo para aprendizado de italiano, construído com LangChain e Gradio, oferecendo uma experiência educativa interativa e personalizada.



## 📋 Visão Geral

O **Tutor de Italiano IA** é uma aplicação educativa avançada que utiliza inteligência artificial para ensinar italiano de forma interativa e personalizada. O projeto combina o poder do modelo Gemini do Google com uma interface web intuitiva criada em Gradio, oferecendo múltiplas funcionalidades educativas em uma arquitetura modular e extensível.

### 🎯 Propósito

Este projeto foi desenvolvido para:
- Fornecer um tutor de italiano disponível 24/7
- Oferecer correções em tempo real de gramática e vocabulário
- Criar uma experiência de aprendizado interativa e envolvente
- Disponibilizar recursos educativos diversificados em uma única plataforma
- Demonstrar a aplicação prática de LangChain e Gradio em projetos educacionais

### ✨ Funcionalidades Principais

1. **Tutor Geral**: Conversação em italiano com correções automáticas de gramática, sintaxe e vocabulário
2. **Tradução Inteligente**: Tradução bidirecional entre italiano e português
3. **Quizzes Interativos**: Geração automática de quizzes de múltipla escolha e preenchimento de lacunas
4. **Aulas de Gramática**: Explicações detalhadas de conceitos gramaticais específicos
5. **Recomendações Culturais**: Sugestões personalizadas de filmes, séries, livros e músicas italianas
6. **Respostas sobre Cultura**: O agente usa seu conhecimento interno para responder perguntas sobre cultura, história e geografia da Itália.

### 🛠️ Tecnologias Utilizadas

- **LangChain**: Framework para desenvolvimento de aplicações com LLM
- **Google Gemini**: Modelo de linguagem avançado via langchain-google-genai
- **Gradio**: Interface web interativa e responsiva
- **Python**: Linguagem de programação principal

## 🔧 Requisitos de Sistema

### Pré-requisitos

- **Python 3.8+**: Versão mínima recomendada
- **Pip**: Gerenciador de pacotes Python
- **Chave da API do Google**: Para acesso ao modelo Gemini
- **Conexão com Internet**: Para funcionalidades de pesquisa e modelo

### Dependências Python

O arquivo `requirements.txt` contém todas as dependências necessárias:

```
langchain
langchain-google-genai
langchain-community
gradio
python-dotenv
beautifulsoup4
```

### Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```env
GOOGLE_API_KEY=sua_chave_da_api_do_google_aqui
```

### Como Obter as Chaves de API

1. **Google API Key (Gemini)**:
   - Acesse [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Crie uma nova chave de API
   - Copie a chave gerada

## 📁 Estrutura de Arquivos

```
tutor-italiano-ia/
├── main.py                     # Ponto de entrada principal da aplicação
├── requirements.txt            # Dependências Python
├── .env                        # Sua configuração de ambiente
├── test_basic_functionality.py # Script de teste básico
├── README.md                  # Documentação principal
│
├── agents/                    # Módulos dos agentes de IA
│   ├── __init__.py
│   ├── gemini_model.py        # Configuração do modelo Gemini
│   ├── general_tutor_agent.py # Agente tutor geral
│   ├── translation_agent.py   # Agente de tradução
│   ├── quiz_agent.py          # Agente de quizzes
│   ├── grammar_agent.py       # Agente de gramática
│   ├── recommendation_agent.py # Agente de recomendações
│   └── router_agent.py        # Agente de roteamento
│
├── prompts/                   # Templates de prompts
│   ├── __init__.py
│   ├── general_tutor_prompts.py
│   ├── translation_prompts.py
│   ├── quiz_prompts.py
│   ├── grammar_prompts.py
│   └── recommendation_prompts.py
│
└── ui/                        # Interface do usuário
    ├── __init__.py
    └── gradio_interface.py     # Interface Gradio principal
```

### Descrição dos Componentes

#### 📂 `agents/`
Contém todos os agentes especializados do sistema:
- **`gemini_model.py`**: Configuração e inicialização do modelo Gemini
- **`general_tutor_agent.py`**: Agente principal para conversação e correções
- **`translation_agent.py`**: Especializado em traduções italiano-português
- **`quiz_agent.py`**: Geração de quizzes educativos
- **`grammar_agent.py`**: Explicações de conceitos gramaticais
- **`recommendation_agent.py`**: Sugestões de conteúdo cultural
- **`router_agent.py`**: Roteamento inteligente de mensagens

#### 📂 `prompts/`
Templates de prompts organizados por funcionalidade, permitindo fácil manutenção e personalização das instruções para cada agente.

#### 📂 `ui/`
Interface do usuário construída com Gradio, oferecendo uma experiência web interativa e responsiva.


## 🚀 Como Executar: Um Guia Detalhado

Para colocar o Tutor de Italiano IA em funcionamento, siga este guia passo a passo. Cada etapa é explicada em detalhes para garantir que você consiga executar o projeto sem problemas.

### 1. Clone ou Baixe o Projeto

**O que é isso?**
É o ato de copiar todos os arquivos do projeto para o seu computador.

**Como fazer:**
Se você tem Git, use o comando `git clone <URL_DO_REPOSITÓRIO>`. Se não, baixe o arquivo `.zip` que enviei e descompacte-o.

### 2. Crie um Ambiente Virtual

**O que é isso?**
É uma "caixa" isolada para as dependências do projeto. Isso evita que as bibliotecas deste projeto interfiram com outros projetos Python que você possa ter.

**Como fazer:**
Abra o terminal (ou Prompt de Comando) na pasta do projeto.
Digite `python -m venv venv`.
Ative-o: no Windows, use `.\venv\Scripts\activate`; no Linux/macOS, use `source venv/bin/activate`.

### 3. Instale as Dependências

**O que é isso?**
O projeto precisa de bibliotecas externas (como LangChain e Gradio) para funcionar. Este passo instala todas elas de uma vez.

**Como fazer:**
Com o ambiente virtual ativado, digite `pip install -r requirements.txt` no terminal. Ele lerá o arquivo `requirements.txt` e instalará tudo o que for necessário.

### 4. Configure as Variáveis de Ambiente

**O que é isso?**
Sua chave de API do Google é um segredo que não deve ser escrito diretamente no código. Nós a armazenamos em um arquivo `.env` que é ignorado pelo sistema de controle de versão.

**Como fazer:**
2. Abra ou crie o arquivo `.env` com um editor de texto.
3. Cole sua chave da API do Google no lugar de `your_google_api_key_here`.

### 5. Execute o Teste Básico (Opcional)

**O que é isso?**
Um script rápido para garantir que tudo foi configurado corretamente antes de iniciar a aplicação completa.

**Como fazer:**
No terminal, digite `python test_basic_functionality.py`. Se aparecerem mensagens de erro, elas indicarão o que deu errado (geralmente, uma dependência faltando ou a chave de API não encontrada).

### 6. Inicie a Aplicação

**O que é isso?**
Este comando inicia o servidor web local que executa a interface do Gradio, tornando o agente acessível no seu navegador.

**Como fazer:**
No terminal, digite `python main.py`. Após algumas mensagens, ele mostrará uma URL local (como `http://127.0.0.1:7860`). Copie e cole essa URL no seu navegador para começar a usar o tutor!

### Acesso à Interface

Após iniciar a aplicação, você verá uma mensagem similar a:

```
🇮🇹 Iniciando o Tutor de Italiano IA...
✅ Variáveis de ambiente configuradas corretamente!
🚀 Carregando a interface...
🌐 Iniciando o servidor...
Running on local URL:  http://127.0.0.1:7860
```

Abra seu navegador e acesse `http://127.0.0.1:7860` para usar a interface.

### Solução de Problemas Comuns

#### Erro: "GOOGLE_API_KEY not found"
- Verifique se o arquivo `.env` existe na raiz do projeto
- Confirme se a variável `GOOGLE_API_KEY` está definida corretamente
- Teste sua chave de API no Google AI Studio

#### Erro: "No module named 'langchain'"
- Execute `pip install -r requirements.txt` novamente
- Verifique se está no ambiente virtual correto

#### Interface não carrega
- Verifique se a porta 7860 não está sendo usada por outro processo
- Tente acessar `http://localhost:7860` em vez de `127.0.0.1`


## 🏗️ Arquitetura

### Visão Geral da Arquitetura

O sistema segue uma arquitetura modular baseada em agentes especializados, promovendo separação de responsabilidades e facilidade de manutenção.

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Interface     │    │   Roteamento    │    │    Agentes      │
│    Gradio       │◄──►│   Inteligente   │◄──►│ Especializados  │
│                 │    │                 │    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       
         │                       │                       
         ▼                       ▼                       
┌─────────────────┐    ┌─────────────────┐    
│   Componentes   │    │    Prompts      │       
│      UI         │    │   Templates     │       
│                 │    │                 │                  
└─────────────────┘    └─────────────────┘   
```

### Fluxo de Dados

1. **Entrada do Usuário**: O usuário interage através da interface Gradio
2. **Roteamento**: O `router_agent` analisa a mensagem e determina qual agente deve processar
3. **Processamento**: O agente especializado processa a solicitação usando prompts específicos
4. **Resposta**: O resultado é formatado e retornado através da interface

### Componentes Principais

#### 🎯 Router Agent
- **Função**: Analisa mensagens do usuário e roteia para o agente apropriado
- **Tecnologia**: LangChain + Gemini
- **Decisões**: Baseadas em análise semântica do conteúdo

#### 🤖 Agentes Especializados
Cada agente tem uma responsabilidade específica:
- **General Tutor**: Conversação geral e correções
- **Translation**: Traduções bidirecionais
- **Quiz**: Geração de exercícios
- **Grammar**: Explicações gramaticais
- **Recommendation**: Sugestões culturais

#### 📝 Sistema de Prompts
- Templates organizados por funcionalidade
- Fácil personalização e manutenção
- Prompts otimizados para cada tipo de tarefa

#### 🔧 Ferramentas
- **Extensível**: Arquitetura permite adição de novas ferramentas

### Vantagens da Arquitetura

1. **Modularidade**: Cada componente tem responsabilidade bem definida
2. **Escalabilidade**: Fácil adição de novos agentes e funcionalidades
3. **Manutenibilidade**: Código organizado e fácil de debugar
4. **Testabilidade**: Componentes podem ser testados independentemente
5. **Flexibilidade**: Prompts e comportamentos facilmente ajustáveis


## 🔧 Como Estender

### Adicionando Novos Agentes

Para criar um novo agente especializado:

1. **Crie o arquivo do agente** em `agents/`:
   ```python
   # agents/novo_agente.py
   from langchain.chains import LLMChain
   from langchain.prompts import PromptTemplate
   from agents.gemini_model import get_gemini_llm
   from prompts.novo_prompt import get_novo_prompt
   
   def create_novo_agente():
       llm = get_gemini_llm()
       prompt = PromptTemplate.from_template(get_novo_prompt())
       return LLMChain(llm=llm, prompt=prompt)
   ```

2. **Crie o template de prompt** em `prompts/`:
   ```python
   # prompts/novo_prompt.py
   def get_novo_prompt():
       return """
       Você é um especialista em [área específica].
       Sua tarefa é [descrição da tarefa].
       
       Input do usuário: {input}
       """
   ```

3. **Atualize o router** em `agents/router_agent.py`:
   ```python
   # Adicione a nova categoria na lista de opções
   - 'nova_categoria': Se o usuário [condição para ativar].
   ```

4. **Integre na interface** em `ui/gradio_interface.py`:
   ```python
   # Importe o novo agente
   from agents.novo_agente import create_novo_agente
   
   # Adicione na classe ItalianTutorInterface
   self.novo_agente = create_novo_agente()
   
   # Adicione no método process_message
   elif route == "nova_categoria":
       response = self.novo_agente.run(input=message)
   ```

### Adicionando Novas Ferramentas

Para criar uma nova ferramenta auxiliar:

1. **Crie a pasta `tools/` (se ainda não existir):**
   ```bash
   mkdir -p tools


2. **Crie o arquivo da ferramenta** em `tools/`:
   ```python
   # tools/nova_ferramenta.py
   import os
   from dotenv import load_dotenv
   
   load_dotenv()
   
   def get_nova_ferramenta():
       # Implementação da ferramenta
       pass
   ```

3. **Integre nos agentes** que precisam da ferramenta:
   ```python
   from tools.nova_ferramenta import get_nova_ferramenta
   
   # Use conforme necessário
   ```

### Personalizando Prompts

Para modificar o comportamento dos agentes:

1. **Edite os arquivos** em `prompts/`:
   ```python
   def get_prompt_personalizado():
       return """
       [Suas instruções personalizadas aqui]
       
       Contexto: {context}
       Pergunta: {question}
       """
   ```

2. **Teste as mudanças** executando o script de teste:
   ```bash
   python test_basic_functionality.py
   ```

### Adicionando Componentes de UI

Para expandir a interface Gradio:

1. **Modifique** `ui/gradio_interface.py`:
   ```python
   # Adicione novos componentes na função create_interface
   with gr.Tab("Nova Funcionalidade"):
       novo_input = gr.Textbox(placeholder="...")
       novo_output = gr.Textbox(label="...")
       novo_btn = gr.Button("Executar")
       novo_btn.click(self.nova_funcao, novo_input, novo_output)
   ```

2. **Implemente a função** correspondente na classe:
   ```python
   def nova_funcao(self, input_text):
       try:
           # Lógica da nova funcionalidade
           return resultado
       except Exception as e:
           return f"Erro: {str(e)}"
   ```

### Configurações Avançadas

#### Modificando o Modelo de IA

Para usar um modelo diferente, edite `agents/gemini_model.py`:

```python
def get_gemini_llm():
    return ChatGoogleGenerativeAI(
        model="gemini-pro-vision",  # Modelo diferente
        temperature=0.7,            # Ajuste de criatividade
        google_api_key=GOOGLE_API_KEY
    )
```

#### Adicionando Logging

Para melhor debugging, adicione logging:

```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Use em seus métodos
logger.info("Processando mensagem do usuário")
```

### Boas Práticas

1. **Teste sempre** novas funcionalidades antes de integrar
2. **Mantenha a modularidade** - cada componente deve ter uma responsabilidade
3. **Documente** mudanças significativas
4. **Use tratamento de erros** adequado
5. **Siga o padrão** de nomenclatura existente


## 🎮 Como Usar

### Interface Principal

A aplicação oferece duas abas principais:

#### 💬 Chat Principal
- **Conversação Natural**: Digite em italiano ou português
- **Correções Automáticas**: O agente corrige erros e explica
- **Roteamento Inteligente**: Mensagens são direcionadas automaticamente

#### ⚡ Ferramentas Rápidas
- **Tradução Rápida**: Tradução instantânea entre idiomas
- **Quiz Rápido**: Geração de exercícios de gramática
- **Recomendações**: Sugestões culturais personalizadas

### Exemplos de Uso

#### Conversação Geral
```
Usuário: "Ciao! Come stai oggi?"
Agente: "Ciao! Sto bene, grazie! E tu come stai? 
         (Pequena correção: em italiano formal seria 'Come sta?')"
```

#### Tradução
```
Usuário: "Traduza: Eu gosto muito de pizza italiana"
Agente: "Mi piace molto la pizza italiana"
```

#### Quiz
```
Usuário: "Quero um quiz sobre verbos"
Agente: "Qual é a conjugação correta do verbo 'essere' na primeira pessoa do singular?
         a) sono  b) sei  c) è  d) siamo
         Resposta correta: a) sono"
```

## 🤝 Contribuição

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 🆘 Suporte

Se encontrar problemas ou tiver dúvidas:

1. Verifique a seção de **Solução de Problemas** acima
2. Execute o script de teste: `python test_basic_functionality.py`
3. Consulte a documentação das dependências:
   - [LangChain](https://python.langchain.com/)
   - [Gradio](https://gradio.app/)
   - [Google AI](https://ai.google.dev/)

## 🙏 Agradecimentos

- **Google**: Pelo modelo Gemini e APIs
- **LangChain**: Framework excepcional para aplicações de IA
- **Gradio**: Interface web simples e poderosa
- **Comunidade Python**: Pelas bibliotecas e ferramentas

---

**Buona fortuna con il tuo apprendimento dell'italiano! 🇮🇹✨**

