import gradio as gr
import json
import re
import os
import uuid
from gtts import gTTS
from agents.general_tutor_agent import create_general_tutor_agent
from agents.translation_agent import create_translation_agent
from agents.quiz_agent import create_quiz_agent
from agents.grammar_agent import create_grammar_agent
from agents.recommendation_agent import create_recommendation_agent
from agents.router_agent import create_router_agent
from agents.roleplay_agent import create_roleplay_agent

# --- Funções de Ajuda ---
def clean_text_for_speech(text):
    if not text:
        return ""
    text = re.sub(r'\*(\*?)(.*?)\1\*', r'\2', text)
    text = re.sub(r'#+\s', '', text)
    text = re.sub(r'\[(.*?)\]\(.*?\)', r'\1', text)
    return text

def text_to_speech(text, lang='it'):
    cleaned_text = clean_text_for_speech(text)
    if not cleaned_text:
        return None
    
    temp_dir = "temp_audio"
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
        
    try:
        tts = gTTS(text=cleaned_text, lang=lang, slow=False)
        filename = os.path.join(temp_dir, f"{uuid.uuid4()}.mp3")
        tts.save(filename)
        return filename
    except Exception as e:
        print(f"Erro no gTTS: {e}")
        return None

custom_css = """
/* (CSS Omitido por Brevidade) */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Poppins:wght@400;500;600;700&display=swap');
body { background: #f0f2f5; font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif; }
.gradio-container { background: #ffffff; border-radius: 16px; box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08); }
.main-heading { font-family: 'Poppins', sans-serif !important; font-size: 3rem !important; font-weight: 700 !important; color: #34495e; text-align: center !important; margin: 20px 0 10px 0 !important; }
.sub-heading { text-align: center !important; color: #64748b !important; font-size: 1.2rem !important; font-weight: 500 !important; margin: 0 0 30px 0 !important; opacity: 0.9 !important; }
.tabs { border-radius: 12px; }
.gradio-tabs-nav button { font-weight: 600; font-family: 'Poppins', sans-serif !important; color: #34495e; transition: all 0.3s ease; }
.gradio-tabs-nav button.selected { color: #4c51bf; border-bottom: 2px solid #4c51bf; background: rgba(76, 81, 191, 0.05); }
.quick-tools-section { background: #fafafa !important; border: 1px solid #e0e0e0 !important; border-radius: 20px !important; padding: 32px !important; margin: 16px !important; transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important; box-shadow: 0 5px 15px rgba(0, 0, 0, 0.05) !important; }
.quick-tools-section:hover { transform: translateY(-5px) !important; box-shadow: 0 15px 30px rgba(0, 0, 0, 0.1) !important; }
.tool-heading { font-family: 'Poppins', sans-serif !important; color: #2d3748 !important; font-size: 1.4rem !important; font-weight: 600 !important; padding-bottom: 8px !important; margin-bottom: 20px !important; border-bottom: 2px solid #e2e8f0; }
.button-primary { background: linear-gradient(135deg, #4c51bf, #667eea) !important; color: white !important; font-weight: 600 !important; border: none !important; border-radius: 14px !important; padding: 14px 28px !important; cursor: pointer !important; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important; box-shadow: 0 4px 15px rgba(79, 70, 229, 0.4) !important; text-transform: uppercase !important; letter-spacing: 0.5px !important; }
.button-primary:hover { transform: translateY(-3px) !important; box-shadow: 0 8px 25px rgba(79, 70, 229, 0.5) !important; }
.gr-button-secondary { background: #f8fafc !important; border: 2px solid #e2e8f0 !important; color: #4a5568 !important; border-radius: 12px !important; font-weight: 500 !important; transition: all 0.3s ease !important; }
.gr-button-secondary:hover { background: #e2e8f0 !important; transform: translateY(-2px) !important; }
.gr-chatbot { border-radius: 20px !important; border: 1px solid #e2e8f0 !important; background: #ffffff !important; }
.gr-textbox { border-radius: 14px !important; border: 2px solid #e2e8f0 !important; background: #ffffff !important; transition: all 0.3s ease !important; padding: 16px !important; }
.gr-textbox:focus { border-color: #4c51bf !important; box-shadow: 0 0 0 4px rgba(79, 70, 229, 0.1) !important; transform: translateY(-1px) !important; }
.gr-chatbot .user-message { background-color: #e3f2fd; border-radius: 15px 15px 0 15px; color: #1a237e; font-weight: 500; }
.gr-chatbot .bot-message { background-color: #e8f5e9; border-radius: 15px 15px 15px 0; color: #1b5e20; font-weight: 500; }
"""

class ItalianTutorInterface:
    def __init__(self):
        self.general_tutor_chain = create_general_tutor_agent()
        self.translation_agent = create_translation_agent()
        self.quiz_agent = create_quiz_agent()
        self.grammar_agent = create_grammar_agent()
        self.recommendation_agent = create_recommendation_agent()
        self.router_agent = create_router_agent()

    def process_message(self, message, history):
        try:
            if not message:
                return history, ""
            route = self.router_agent.run(user_input=message).strip().lower()
            response = ""
            if route == "traducao":
                response = self.translation_agent.run(text=message, language="auto")
            elif route == "quiz":
                response = "Você pode iniciar um quiz na aba 'Ferramentas Rápidas'!"
            elif route == "gramatica":
                response = self.grammar_agent.run(concept=message)
            elif route == "recomendacao":
                response = self.recommendation_agent.run(interest=message)
            elif route == "pesquisa":
                response = self.general_tutor_chain.predict(input=f"Responda a seguinte pergunta sobre cultura italiana: {message}")
            else: 
                response = self.general_tutor_chain.predict(input=message)
            history.append([message, response])
            return history, ""
        except Exception as e:
            error_message = f"❌ Desculpe, ocorreu um erro inesperado: {str(e)}"
            history.append([message, error_message])
            return history, ""
    
    def generate_audio_from_selection(self, evt: gr.SelectData):
        if evt.value and evt.index[1] is not None:
            bot_message = evt.value
            audio_path = text_to_speech(bot_message)
            return gr.Audio(value=audio_path, autoplay=True, interactive=False)
        return None

    def quick_translation(self, text):
        if not text:
            return "📝 Por favor, digite o texto para traduzir."
        try:
            return self.translation_agent.run(text=text, language="auto")
        except Exception as e:
            return f"❌ Erro na tradução: {str(e)}"

    def quick_recommendation(self, interest):
        if not interest:
            return "🎯 Por favor, digite seus interesses para receber recomendações."
        try:
            return self.recommendation_agent.run(interest=interest)
        except Exception as e:
            return f"❌ Erro ao gerar recomendação: {str(e)}"

    def _setup_question_ui(self, question):
        """Função auxiliar para configurar a UI para a pergunta atual."""
        if question['type'] == 'multipla_escolha':
            return {
                quiz_question_text: question["pergunta"],
                quiz_choices: gr.update(choices=question["alternativas"], value=None, interactive=True, visible=True),
                quiz_fill_in_input: gr.update(visible=False, value=""),
            }
        elif question['type'] == 'preencher_lacuna':
            return {
                quiz_question_text: question["pergunta"],
                quiz_choices: gr.update(visible=False, value=None),
                quiz_fill_in_input: gr.update(visible=True, value="", interactive=True, placeholder="Digite a palavra que falta..."),
            }
        return {}

    def start_quiz(self, topic):
        if not topic:
            topic = "cultura e gramática básica"
        try:
            raw_response = self.quiz_agent.run(topic=topic)
            json_match = re.search(r'```json\n({.*?})\n```', raw_response, re.DOTALL)
            json_str = json_match.group(1) if json_match else raw_response
            quiz_data = json.loads(json_str)
            
            score = 0
            current_question_index = 0
            first_question = quiz_data["quiz"][current_question_index]
            
            updates = self._setup_question_ui(first_question)
            updates.update({
                quiz_data_state: quiz_data,
                quiz_score_state: score,
                quiz_question_index_state: current_question_index,
                quiz_container: gr.update(visible=True),
                start_quiz_wrapper: gr.update(visible=False),
                quiz_feedback_text: "",
                quiz_submit_button: gr.update(visible=True),
                quiz_next_button: gr.update(visible=False),
                quiz_summary_text: ""
            })
            return updates
        except Exception as e:
            error_message = f"❌ Desculpe, não consegui gerar o quiz. Tente novamente.\nErro: {str(e)}"
            return {
                quiz_container: gr.update(visible=False),
                start_quiz_wrapper: gr.update(visible=True),
                quiz_summary_text: error_message
            }

    def submit_answer(self, mc_choice, fill_in_answer, quiz_data, current_question_index, score):
        question_info = quiz_data["quiz"][current_question_index]
        correct_answer = question_info["resposta_correta"]
        user_answer = ""

        if question_info['type'] == 'multipla_escolha':
            user_answer = mc_choice
        elif question_info['type'] == 'preencher_lacuna':
            user_answer = fill_in_answer.strip()

        # Comparação flexível
        if user_answer.lower() == correct_answer.lower():
            score += 1
            feedback = f"<h3>✅ Correto!</h3><p>{question_info['explicacao']}</p>"
        else:
            feedback = f"<h3>❌ Incorreto.</h3><p>A resposta correta é: <b>{correct_answer}</b>.</p><p>{question_info['explicacao']}</p>"

        return {
            quiz_score_state: score,
            quiz_feedback_text: feedback,
            quiz_submit_button: gr.update(visible=False),
            quiz_next_button: gr.update(visible=True),
            quiz_choices: gr.update(interactive=False),
            quiz_fill_in_input: gr.update(interactive=False)
        }
        
    def next_question(self, quiz_data, current_question_index, score):
        current_question_index += 1
        
        if current_question_index < len(quiz_data["quiz"]):
            next_q = quiz_data["quiz"][current_question_index]
            updates = self._setup_question_ui(next_q)
            updates.update({
                quiz_question_index_state: current_question_index,
                quiz_feedback_text: "",
                quiz_submit_button: gr.update(visible=True),
                quiz_next_button: gr.update(visible=False)
            })
            return updates
        else:
            total_questions = len(quiz_data["quiz"])
            summary = f"<h2>🎉 Quiz Finalizado!</h2><h3>Sua pontuação: {score} de {total_questions}</h3>"
            return {
                quiz_container: gr.update(visible=False),
                start_quiz_wrapper: gr.update(visible=True),
                quiz_summary_text: summary,
                quiz_feedback_text: ""
            }

    # --- Funções para o Agente de Role-Play ---
    def start_simulation(self, scenario):
        if not scenario:
            return None, None, gr.update(visible=True), gr.update(visible=False)
        try:
            agent = create_roleplay_agent()
            initial_response = agent.predict(input=scenario)
            initial_history = [[None, initial_response]]
            return agent, initial_history, gr.update(visible=False), gr.update(visible=True)
        except Exception as e:
            print(f"Erro ao iniciar simulação: {e}")
            return None, None, gr.update(visible=True), gr.update(visible=False)

    def process_roleplay_message(self, message, history, agent):
        if not message or not agent:
            return history, ""
        try:
            response = agent.predict(input=message)
            history.append([message, response])
            return history, ""
        except Exception as e:
            error_message = f"❌ Desculpe, ocorreu um erro na simulação: {str(e)}"
            history.append([message, error_message])
            return history, ""

    def end_simulation(self):
        return None, [], gr.update(visible=True), gr.update(visible=False), ""

    def create_interface(self):
        with gr.Blocks(title="🇮🇹 Tutor de Italiano IA", theme=gr.themes.Soft(primary_hue="indigo", secondary_hue="blue", neutral_hue="slate"), css=custom_css) as interface:
            gr.Markdown("# <span class='main-heading'>🇮🇹 Tutor de Italiano IA</span>")
            gr.Markdown("<span class='sub-heading'>Sua jornada personalizada para dominar o italiano com inteligência artificial 🚀</span>")

            global quiz_data_state, quiz_score_state, quiz_question_index_state
            quiz_data_state = gr.State()
            quiz_score_state = gr.State()
            quiz_question_index_state = gr.State()
            roleplay_agent_state = gr.State()

            with gr.Tabs(elem_classes=["tabs"]):
                with gr.TabItem("💬 Chat Inteligente"):
                    chatbot = gr.Chatbot(height=500, label="💬 Conversa com seu Tutor Pessoal", avatar_images=("https://cdn-icons-png.flaticon.com/512/3233/3233519.png", "https://cdn-icons-png.flaticon.com/512/4712/4712030.png"), bubble_full_width=False, render_markdown=True)
                    audio_output = gr.Audio(label="🎧 Para ouvir, clique em uma mensagem do tutor", interactive=False)
                    with gr.Row():
                        with gr.Column(scale=4):
                            msg = gr.Textbox(placeholder="💭 Pergunte sobre gramática, peça traduções ou apenas converse em italiano...", show_label=False)
                        with gr.Column(scale=1):
                            send_btn = gr.Button("Enviar 🚀", elem_classes=["button-primary"])
                    clear = gr.Button("🗑️ Limpar Chat", elem_classes=["gr-button-secondary"])

                with gr.TabItem("🎭 Simulação (Role-play)"):
                    with gr.Column() as roleplay_setup_wrapper:
                        gr.Markdown("### <span class='tool-heading'>🎭 Prática de Conversação</span>")
                        rp_scenario_input = gr.Textbox(placeholder="Ex: Em um restaurante pedindo uma pizza, comprando um bilhete de trem...", label="✍️ Descreva o cenário que você quer praticar:")
                        rp_start_btn = gr.Button("🎬 Iniciar Simulação", elem_classes=["button-primary"])
                    with gr.Column(visible=False) as roleplay_chat_wrapper:
                        rp_chatbot = gr.Chatbot(height=450, label="🎭 Simulação em Andamento", avatar_images=("https-icons-png.flaticon.com/512/3233/3233519.png", "https-icons-png.flaticon.com/512/1211/1211019.png"), bubble_full_width=False, render_markdown=True)
                        rp_audio_output = gr.Audio(label="🎧 Para ouvir, clique em uma mensagem do ator", interactive=False)
                        with gr.Row():
                            with gr.Column(scale=4):
                                rp_msg = gr.Textbox(placeholder="Digite sua resposta em italiano...", show_label=False)
                            with gr.Column(scale=1):
                                rp_send_btn = gr.Button("Enviar 💬", elem_classes=["button-primary"])
                        rp_end_btn = gr.Button("🎉 Terminar Simulação", elem_classes=["gr-button-secondary"])
                
                with gr.TabItem("⚡ Ferramentas Rápidas"):
                    with gr.Row():
                        with gr.Column(elem_classes=["quick-tools-section"]):
                            gr.Markdown("### <span class='tool-heading'>🔄 Tradutor Profissional</span>")
                            translation_input = gr.Textbox(placeholder="✍️ Digite ou cole o texto...", label="📝 Texto para Tradução", lines=3)
                            translation_output = gr.Textbox(label="🎯 Resultado", interactive=False, lines=4)
                            translate_btn = gr.Button("🔄 Traduzir Agora", elem_classes=["button-primary"])
                        with gr.Column(elem_classes=["quick-tools-section"]):
                            gr.Markdown("### <span class='tool-heading'>🧠 Quiz Interativo</span>")
                            global start_quiz_wrapper, quiz_summary_text, quiz_container, quiz_question_text, quiz_choices, quiz_fill_in_input, quiz_feedback_text, quiz_submit_button, quiz_next_button
                            with gr.Column(visible=True) as start_quiz_wrapper:
                                quiz_topic_input = gr.Textbox(placeholder="Ex: verbos, artigos, preposições...", label="Tópico do Quiz (opcional)")
                                quiz_btn = gr.Button("🎲 Gerar Novo Quiz", elem_classes=["button-primary"])
                                quiz_summary_text = gr.Markdown()
                            with gr.Column(visible=False) as quiz_container:
                                quiz_question_text = gr.Markdown("### Pergunta do Quiz Aqui")
                                quiz_choices = gr.Radio(label="Escolha uma alternativa:", interactive=True, visible=False)
                                quiz_fill_in_input = gr.Textbox(label="Sua resposta:", interactive=True, visible=False)
                                quiz_feedback_text = gr.Markdown()
                                with gr.Row():
                                    quiz_submit_button = gr.Button("Responder", elem_classes=["button-primary"])
                                    quiz_next_button = gr.Button("Próxima Pergunta →", visible=False)
                    with gr.Row():
                        with gr.Column(elem_classes=["quick-tools-section"]):
                             gr.Markdown("### <span class='tool-heading'>✨ Recomendações IA</span>")
                             interest_input = gr.Textbox(placeholder="🎬 Ex: cinema, música, culinária...", label="🎯 Seus Interesses")
                             recommendation_output = gr.Textbox(label="🌟 Recomendações", interactive=False, lines=6)
                             recommend_btn = gr.Button("✨ Descobrir Conteúdo", elem_classes=["button-primary"])
            
            # --- Event Listeners ---
            msg.submit(self.process_message, [msg, chatbot], [chatbot, msg])
            send_btn.click(self.process_message, [msg, chatbot], [chatbot, msg])
            clear.click(lambda: (None), None, [chatbot], queue=False)
            chatbot.select(self.generate_audio_from_selection, None, audio_output)

            translate_btn.click(self.quick_translation, translation_input, translation_output)
            recommend_btn.click(self.quick_recommendation, interest_input, recommendation_output)
            
            quiz_btn.click(self.start_quiz, inputs=[quiz_topic_input], outputs=[quiz_data_state, quiz_score_state, quiz_question_index_state, quiz_container, start_quiz_wrapper, quiz_question_text, quiz_choices, quiz_fill_in_input, quiz_feedback_text, quiz_submit_button, quiz_next_button, quiz_summary_text])
            quiz_submit_button.click(self.submit_answer, inputs=[quiz_choices, quiz_fill_in_input, quiz_data_state, quiz_question_index_state, quiz_score_state], outputs=[quiz_score_state, quiz_feedback_text, quiz_submit_button, quiz_next_button, quiz_choices, quiz_fill_in_input])
            quiz_next_button.click(self.next_question, inputs=[quiz_data_state, quiz_question_index_state, quiz_score_state], outputs=[quiz_question_index_state, quiz_question_text, quiz_choices, quiz_fill_in_input, quiz_feedback_text, quiz_submit_button, quiz_next_button, quiz_container, start_quiz_wrapper, quiz_summary_text])

            rp_start_btn.click(self.start_simulation, inputs=[rp_scenario_input], outputs=[roleplay_agent_state, rp_chatbot, roleplay_setup_wrapper, roleplay_chat_wrapper])
            rp_msg.submit(self.process_roleplay_message, [rp_msg, rp_chatbot, roleplay_agent_state], [rp_chatbot, rp_msg])
            rp_send_btn.click(self.process_roleplay_message, [rp_msg, rp_chatbot, roleplay_agent_state], [rp_chatbot, rp_msg])
            rp_chatbot.select(self.generate_audio_from_selection, None, rp_audio_output)
            rp_end_btn.click(self.end_simulation, inputs=[], outputs=[roleplay_agent_state, rp_chatbot, roleplay_setup_wrapper, roleplay_chat_wrapper, rp_scenario_input])

        return interface

def create_gradio_app():
    tutor = ItalianTutorInterface()
    return tutor.create_interface()