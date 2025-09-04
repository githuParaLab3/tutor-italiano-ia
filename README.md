🇮🇹 Tutor de Italiano IA Um agente de IA completo para aprendizado de
italiano, construído com LangChain e Gradio, oferecendo uma experiência
educativa interativa, estruturada e personalizada.

📋 Visão Geral O Tutor de Italiano IA é uma aplicação educativa avançada
que utiliza inteligência artificial para ensinar italiano de forma
interativa e personalizada. O projeto combina o poder do modelo Gemini
do Google com uma interface web intuitiva criada em Gradio, oferecendo
múltiplas funcionalidades educativas numa arquitetura modular e
extensível.

🎯 Propósito Este projeto foi desenvolvido para: - Fornecer um tutor de
italiano disponível 24/7. - Oferecer uma experiência de aprendizado
estruturada com planos de estudo. - Criar um ambiente seguro para a
prática de conversação através de simulações. - Disponibilizar recursos
educativos diversificados numa única plataforma. - Demonstrar a
aplicação prática de LangChain e Gradio em projetos educacionais.

✨ Funcionalidades Principais - **Chat Inteligente com Memória**:
Converse em italiano com um tutor que se lembra do contexto da conversa,
oferece correções e explicações gramaticais. - **Plano de Estudos
Estruturado**: Siga um currículo completo do nível A1 ao C2, com lições
detalhadas sobre gramática e vocabulário para cada tópico. - **Simulação
de Conversas (Role-play)**: Pratique o seu italiano em cenários do dia a
dia, como pedir num café ou resolver um problema num hotel, interagindo
com a IA. - **Tradução com Contexto**: Traduções entre português e
italiano que vão além do literal, explicando expressões idiomáticas e
nuances culturais. - **Quizzes Dinâmicos**: Teste os seus conhecimentos
com quizzes interativos que incluem perguntas de múltipla escolha e de
preenchimento de lacunas. - **Recomendações Culturais**: Receba
sugestões de filmes, séries, livros e músicas italianas, com detalhes
sobre o nível de dificuldade e onde encontrar. - **Prática de Pronúncia
(Text-to-Speech)**: Ouça a pronúncia correta de qualquer resposta do
tutor simplesmente clicando na mensagem.

🛠️ Tecnologias Utilizadas - **LangChain**: Framework para
desenvolvimento de aplicações com LLMs. - **Google Gemini**: Modelo de
linguagem avançado via langchain-google-genai. - **Gradio**: Interface
web interativa e responsiva. - **gTTS**: Biblioteca do Google para
funcionalidade de Text-to-Speech. - **Python**: Linguagem de programação
principal.

🔧 Requisitos de Sistema **Pré-requisitos** - Python 3.8+: Versão mínima
recomendada. - Pip: Gestor de pacotes Python. - Chave da API do Google:
Para acesso ao modelo Gemini.

**Dependências Python** O ficheiro `requirements.txt` contém todas as
dependências necessárias:

    langchain
    langchain-google-genai
    langchain-community
    gradio
    python-dotenv
    beautifulsoup4
    gTTS

**Variáveis de Ambiente** Crie um ficheiro `.env` na raiz do projeto com
a sua chave da API do Google:

    GOOGLE_API_KEY=sua_chave_da_api_do_google_aqui

📁 Estrutura de Ficheiros O projeto foi refatorado para uma arquitetura
mais limpa e modular, especialmente na interface do utilizador.

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
    │   ├── grammar_prompts.py
    │   ├── lessons_prompts.py
    │   └── ... (outros ficheiros de prompts)
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

🚀 Como Executar: Um Guia Detalhado Para colocar o Tutor de Italiano IA
em funcionamento, siga este guia passo a passo.

1.  **Clone ou Baixe o Projeto**

    -   Com Git: `git clone <URL_DO_REPOSITORIO>`
    -   Sem Git: baixe e descompacte o `.zip`.

2.  **Crie um Ambiente Virtual**

    ``` bash
    python -m venv venv
    ```

    Ative-o:

    -   Windows: `.env\Scriptsctivate`
    -   Linux/macOS: `source venv/bin/activate`

3.  **Instale as Dependências**

    ``` bash
    pip install -r requirements.txt
    ```

4.  **Configure as Variáveis de Ambiente** Crie ou edite o ficheiro
    `.env` na pasta do projeto e adicione a sua chave da API do Google:

        GOOGLE_API_KEY=your_google_api_key_here

5.  **Execute o Teste Básico (Opcional)**

    ``` bash
    python test_basic_functionality.py
    ```

6.  **Inicie a Aplicação**

    ``` bash
    python main.py
    ```

    Após algumas mensagens, será exibida uma URL local, normalmente:
    `http://127.0.0.1:7860`.

🎮 Como Usar A interface agora oferece abas dedicadas para diferentes
modos de aprendizado:

-   💬 **Chat Inteligente**
    -   Converse livremente com o tutor.
    -   Peça explicações, traduções ou correções.
    -   Clique em qualquer resposta do tutor para ouvir a pronúncia.
-   📚 **Plano de Estudos**
    -   Escolha o seu nível de proficiência (A1 a C2).
    -   Selecione um tópico da lista para aquele nível.
    -   Receba uma lição completa e estruturada sobre o tema.
-   🎭 **Simulação (Role-play)**
    -   Descreva um cenário que queira praticar.
    -   A IA assumirá um papel e iniciará uma conversa realista.
-   ⚡ **Ferramentas Rápidas**
    -   Tradutor com contexto.
    -   Quizzes dinâmicos.
    -   Recomendações culturais.

🤝 Contribuição Contribuições são bem-vindas! Para contribuir: 1. Faça
um fork do projeto 2. Crie uma branch para a sua feature
(`git checkout -b feature/nova-funcionalidade`) 3. Commit as suas
mudanças (`git commit -am 'Adiciona nova funcionalidade'`) 4. Push para
a branch (`git push origin feature/nova-funcionalidade`) 5. Abra um Pull
Request

📄 Licença Este projeto está sob a licença MIT.

Buona fortuna con il tuo apprendimento dell'italiano! 🇮🇹✨
