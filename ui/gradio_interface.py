import gradio as gr
from agents.general_tutor_agent import create_general_tutor_agent
from agents.translation_agent import create_translation_agent
from agents.quiz_agent import create_quiz_agent
from agents.grammar_agent import create_grammar_agent
from agents.recommendation_agent import create_recommendation_agent
from agents.router_agent import create_router_agent
from tools.web_search import get_web_search_tool

# CSS profissional, combinando os melhores elementos dos estilos
custom_css = """
/* Importação de fontes Google */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Poppins:wght@400;500;600;700&display=swap');

/* Fundo suave e degradê sutil */
body {
    background: #f0f2f5;
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
}

/* Contêiner principal com sombra e bordas arredondadas */
.gradio-container {
    background: #ffffff;
    border-radius: 16px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08);
    transition: transform 0.3s ease;
}

.gradio-container:hover {
    transform: translateY(-3px);
}

/* Cabeçalho principal com gradiente suave */
.main-heading {
    font-family: 'Poppins', sans-serif !important;
    font-size: 3rem !important;
    font-weight: 700 !important;
    color: #34495e; /* Cor do texto normal para não afetar o emoji */
    text-align: center !important;
    margin: 20px 0 10px 0 !important;
}

.sub-heading {
    text-align: center !important;
    color: #64748b !important;
    font-size: 1.2rem !important;
    font-weight: 500 !important;
    margin: 0 0 30px 0 !important;
    opacity: 0.9 !important;
}

/* Abas */
.tabs {
    border-radius: 12px;
}
.gradio-tabs-nav button {
    font-weight: 600;
    font-family: 'Poppins', sans-serif !important;
    color: #34495e;
    transition: all 0.3s ease;
}
.gradio-tabs-nav button.selected {
    color: #4c51bf;
    border-bottom: 2px solid #4c51bf;
    background: rgba(76, 81, 191, 0.05);
}

/* Cards das ferramentas com design minimalista */
.quick-tools-section {
    background: #fafafa !important;
    border: 1px solid #e0e0e0 !important;
    border-radius: 20px !important;
    padding: 32px !important;
    margin: 16px !important;
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.05) !important;
}

.quick-tools-section:hover {
    transform: translateY(-5px) !important;
    box-shadow: 0 15px 30px rgba(0, 0, 0, 0.1) !important;
}

/* Títulos das ferramentas com linha inferior sutil */
.tool-heading {
    font-family: 'Poppins', sans-serif !important;
    color: #2d3748 !important;
    font-size: 1.4rem !important;
    font-weight: 600 !important;
    padding-bottom: 8px !important;
    margin-bottom: 20px !important;
    border-bottom: 2px solid #e2e8f0;
}

/* Botões principais com gradiente e efeito de pulso */
.button-primary {
    background: linear-gradient(135deg, #4c51bf, #667eea) !important;
    color: white !important;
    font-weight: 600 !important;
    border: none !important;
    border-radius: 14px !important;
    padding: 14px 28px !important;
    cursor: pointer !important;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    box-shadow: 0 4px 15px rgba(79, 70, 229, 0.4) !important;
    text-transform: uppercase !important;
    letter-spacing: 0.5px !important;
}

.button-primary:hover {
    transform: translateY(-3px) !important;
    box-shadow: 0 8px 25px rgba(79, 70, 229, 0.5) !important;
}

/* Botões secundários */
.gr-button-secondary {
    background: #f8fafc !important;
    border: 2px solid #e2e8f0 !important;
    color: #4a5568 !important;
    border-radius: 12px !important;
    font-weight: 500 !important;
    transition: all 0.3s ease !important;
}

.gr-button-secondary:hover {
    background: #e2e8f0 !important;
    transform: translateY(-2px) !important;
}

/* Chatbot e Inputs */
.gr-chatbot {
    border-radius: 20px !important;
    border: 1px solid #e2e8f0 !important;
    background: #ffffff !important;
}
.gr-textbox {
    border-radius: 14px !important;
    border: 2px solid #e2e8f0 !important;
    background: #ffffff !important;
    transition: all 0.3s ease !important;
    padding: 16px !important;
}
.gr-textbox:focus {
    border-color: #4c51bf !important;
    box-shadow: 0 0 0 4px rgba(79, 70, 229, 0.1) !important;
    transform: translateY(-1px) !important;
}

/* Mensagens do chat com design limpo */
.gr-chatbot .user-message {
    background-color: #e3f2fd;
    border-radius: 15px 15px 0 15px;
    color: #1a237e;
    font-weight: 500;
}
.gr-chatbot .bot-message {
    background-color: #e8f5e9;
    border-radius: 15px 15px 15px 0;
    color: #1b5e20;
    font-weight: 500;
}

/* Animações suaves de entrada */
@keyframes fadeInScale {
    from { opacity: 0; transform: scale(0.98); }
    to { opacity: 1; transform: scale(1); }
}
.gradio-container {
    animation: fadeInScale 0.8s ease-out;
}
"""

class ItalianTutorInterface:
    def __init__(self):
        self.general_tutor = create_general_tutor_agent()
        self.translation_agent = create_translation_agent()
        self.quiz_agent = create_quiz_agent()
        self.grammar_agent = create_grammar_agent()
        self.recommendation_agent = create_recommendation_agent()
        self.router_agent = create_router_agent()
        try:
            self.web_search = get_web_search_tool()
        except ValueError:
            self.web_search = None
            print("Ferramenta de pesquisa web não disponível. Por favor, defina GOOGLE_CSE_ID e GOOGLE_API_KEY.")

    def process_message(self, message, history):
        try:
            if not message:
                return history, ""
            route = self.router_agent.run(user_input=message).strip().lower()
            if route == "traducao":
                response = self.translation_agent.run(text=message, language="auto")
            elif route == "quiz":
                response = self.quiz_agent.run(quiz_type="múltipla escolha", topic="gramática italiana")
            elif route == "gramatica":
                response = self.grammar_agent.run(concept=message)
            elif route == "recomendacao":
                response = self.recommendation_agent.run(interest=message)
            elif route == "pesquisa" and self.web_search:
                search_results = self.web_search.run(message)
                response = f"Resultados da pesquisa: {search_results}"
            else:
                response = self.general_tutor.run(text=message)
            history.append([message, response])
            return history, ""
        except Exception as e:
            error_message = f"❌ Desculpe, ocorreu um erro inesperado: {str(e)}"
            history.append([message, error_message])
            return history, ""

    def quick_translation(self, text):
        if not text:
            return "📝 Por favor, digite o texto para traduzir."
        try:
            return self.translation_agent.run(text=text, language="auto")
        except Exception as e:
            return f"❌ Erro na tradução: {str(e)}"

    def quick_quiz(self):
        try:
            return self.quiz_agent.run(quiz_type="múltipla escolha", topic="gramática italiana")
        except Exception as e:
            return f"❌ Erro ao gerar quiz: {str(e)}"

    def quick_recommendation(self, interest):
        if not interest:
            return "🎯 Por favor, digite seus interesses para receber recomendações."
        try:
            return self.recommendation_agent.run(interest=interest)
        except Exception as e:
            return f"❌ Erro ao gerar recomendação: {str(e)}"

    def create_interface(self):
        with gr.Blocks(
            title="🇮🇹 Tutor de Italiano IA - Estilo Master Ultimate",
            theme=gr.themes.Soft(
                primary_hue="indigo",
                secondary_hue="blue",
                neutral_hue="slate"
            ),
            css=custom_css
        ) as interface:
            # Header principal elegante
            # Removido o gradiente de texto para manter a cor original do emoji
            gr.Markdown("# <span class='main-heading'>🇮🇹 Tutor de Italiano IA</span>")
            gr.Markdown("<span class='sub-heading'>Sua jornada personalizada para dominar o italiano com inteligência artificial 🚀</span>")

            tips_visible_state = gr.State(False)

            with gr.Tabs(elem_classes=["tabs"]):
                # Chat principal aprimorado
                with gr.TabItem("💬 Chat Inteligente"):
                    gr.Markdown("### 🤖 Converse naturalmente e deixe a IA decidir como melhor te ajudar!")
                    chatbot = gr.Chatbot(
                        height=500,
                        label="💬 Conversa com seu Tutor Pessoal",
                        avatar_images=(
                            "https://cdn-icons-png.flaticon.com/512/3233/3233519.png", # Ícone de usuário
                            "https://cdn-icons-png.flaticon.com/512/4712/4712030.png"  # Ícone do bot
                        ),
                        bubble_full_width=False
                    )
                    with gr.Row():
                        with gr.Column(scale=4):
                            msg = gr.Textbox(
                                placeholder="💭 Pergunte sobre gramática, peça traduções, solicite quizzes ou apenas converse em italiano...",
                                show_label=False
                            )
                        with gr.Column(scale=1):
                            send_btn = gr.Button("Enviar 🚀", elem_classes=["button-primary"])

                    with gr.Row():
                        clear = gr.Button("🗑️ Limpar Chat", elem_classes=["gr-button-secondary"])
                        help_btn = gr.Button("💡 Dicas de Uso", elem_classes=["gr-button-secondary"])

                    tips_area = gr.Markdown(
                        """
                        ### 💡 Dicas para Usar o Chat:
                        - **Para traduções**: "Traduza 'Ciao come stai?'"
                        - **Para gramática**: "Explique o passato prossimo"
                        - **Para quiz**: "Quero fazer um quiz sobre verbos"
                        - **Para recomendações**: "Recomende filmes italianos"
                        - **Conversa livre**: Escreva em italiano ou português!
                        
                        🎯 **Atalhos**: Ctrl+Enter para enviar | Ctrl+L para limpar
                        """,
                        visible=False
                    )

                # Ferramentas rápidas redesenhadas
                with gr.TabItem("⚡ Ferramentas Rápidas"):
                    with gr.Row():
                        # Tradutor profissional
                        with gr.Column(elem_classes=["quick-tools-section"]):
                            gr.Markdown("### <span class='tool-heading'>🔄 Tradutor Profissional</span>")
                            gr.Markdown("*Sistema avançado de tradução com detecção automática de idioma*")
                            translation_input = gr.Textbox(
                                placeholder="✍️ Digite ou cole o texto que deseja traduzir...",
                                label="📝 Texto para Tradução",
                                lines=3
                            )
                            translation_output = gr.Textbox(
                                label="🎯 Resultado da Tradução",
                                interactive=False,
                                lines=4
                            )
                            translate_btn = gr.Button("🔄 Traduzir Agora", elem_classes=["button-primary"])

                        # Gerador de quiz inteligente
                        with gr.Column(elem_classes=["quick-tools-section"]):
                            gr.Markdown("### <span class='tool-heading'>🧠 Quiz Inteligente</span>")
                            gr.Markdown("*Quizzes adaptativos para testar seu conhecimento*")
                            quiz_output = gr.Textbox(
                                label="🎲 Seu Quiz Personalizado",
                                interactive=False,
                                lines=6
                            )
                            quiz_btn = gr.Button("🎲 Gerar Novo Quiz", elem_classes=["button-primary"])

                    with gr.Row():
                        # Recomendações personalizadas
                        with gr.Column(elem_classes=["quick-tools-section"]):
                            gr.Markdown("### <span class='tool-heading'>✨ Recomendações IA</span>")
                            gr.Markdown("*Descubra conteúdo italiano baseado em seus gostos*")
                            interest_input = gr.Textbox(
                                placeholder="🎬 Ex: cinema, música, culinária, arte, história...",
                                label="🎯 Seus Interesses"
                            )
                            recommendation_output = gr.Textbox(
                                label="🌟 Recomendações Personalizadas",
                                interactive=False,
                                lines=6
                            )
                            recommend_btn = gr.Button("✨ Descobrir Conteúdo", elem_classes=["button-primary"])

            # Configuração dos eventos
            msg.submit(self.process_message, [msg, chatbot], [chatbot, msg])
            send_btn.click(self.process_message, [msg, chatbot], [chatbot, msg])
            clear.click(lambda: [], None, chatbot, queue=False)

            # Ação de clique para alternar as dicas
            help_btn.click(
                lambda visible: not visible,
                inputs=tips_visible_state,
                outputs=tips_visible_state,
                queue=False,
                api_name=False
            ).then(
                lambda visible: gr.update(visible=visible),
                inputs=tips_visible_state,
                outputs=tips_area,
                queue=False,
                api_name=False
            )

            # Ferramentas rápidas
            translate_btn.click(self.quick_translation, translation_input, translation_output)
            quiz_btn.click(self.quick_quiz, None, quiz_output)
            recommend_btn.click(self.quick_recommendation, interest_input, recommendation_output)

        return interface

def create_gradio_app():
    tutor = ItalianTutorInterface()
    return tutor.create_interface()