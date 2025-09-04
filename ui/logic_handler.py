import gradio as gr
import json
import re
import uuid

from agents.general_tutor_agent import create_general_tutor_agent
from agents.translation_agent import create_translation_agent
from agents.quiz_agent import create_quiz_agent
from agents.grammar_agent import create_grammar_agent
from agents.recommendation_agent import create_recommendation_agent
from agents.router_agent import create_router_agent
from agents.roleplay_agent import create_roleplay_agent
from agents.lessons_agent import create_lessons_agent

from core.curriculum import get_topics_for_level
from .helpers import text_to_speech
from langchain_core.messages import HumanMessage, AIMessage

class LogicHandler:
    """
    Esta classe contém toda a lógica de backend da interface Gradio.
    Ela lida com as chamadas aos agentes e o processamento de dados,
    separando a lógica da apresentação da UI.
    """
    def __init__(self):
        self.general_tutor_chain = create_general_tutor_agent()
        self.translation_agent = create_translation_agent()
        self.quiz_agent = create_quiz_agent()
        self.grammar_agent = create_grammar_agent()
        self.recommendation_agent = create_recommendation_agent()
        self.router_agent = create_router_agent()
        self.lessons_agent = create_lessons_agent()
        self.roleplay_agent = create_roleplay_agent()
        self.general_chat_session_id = str(uuid.uuid4())
        self.roleplay_session_id = None

    def process_message(self, message, history):
        history.append({"role": "user", "content": message})
        history.append({"role": "assistant", "content": " Pensando..."})
        yield history, ""

        try:
            if not message:
                history.pop()
                yield history, ""
                return

            route = self.router_agent.invoke({"user_input": message}).content.strip().lower()
            response = ""

            if route == "traducao":
                response = self.translation_agent.invoke({"text": message, "language": "auto"}).content
            elif route == "quiz":
                response = "Você pode iniciar um quiz na aba 'Ferramentas Rápidas'!"
            elif route == "gramatica":
                response = self.grammar_agent.invoke({"concept": message}).content
            elif route == "recomendacao":
                response = self.recommendation_agent.invoke({"interest": message}).content
            elif route == "pesquisa":
                response = self.general_tutor_chain.invoke({"input": f"Responda a seguinte pergunta sobre cultura italiana: {message}"}, config={"configurable": {"session_id": self.general_chat_session_id}}).content
            else:
                response = self.general_tutor_chain.invoke({"input": message}, config={"configurable": {"session_id": self.general_chat_session_id}}).content

            history[-1]["content"] = response
            yield history, ""

        except Exception as e:
            error_message = f" Desculpe, ocorreu um erro inesperado: {str(e)}"
            if history:
                history[-1]["content"] = error_message
            else:
                history.append({"role": "user", "content": message})
                history.append({"role": "assistant", "content": error_message})
            yield history, ""
    
    def generate_audio_from_selection(self, evt: gr.SelectData):
        if evt.value:
            bot_message = evt.value
            audio_path = text_to_speech(bot_message)
            return gr.Audio(value=audio_path, autoplay=True, interactive=False)
        return None

    def quick_translation(self, text):
        if not text:
            yield " Por favor, digite o texto para traduzir."
            return
        yield " Traduzindo..."
        try:
            yield self.translation_agent.invoke({"text": text, "language": "auto"}).content
        except Exception as e:
            yield f" Erro na tradução: {str(e)}"

    def quick_recommendation(self, interest):
        if not interest:
            yield " Por favor, digite seus interesses para receber recomendações."
            return
        yield " Buscando recomendações..."
        try:
            yield self.recommendation_agent.invoke({"interest": interest}).content
        except Exception as e:
            yield f" Erro ao gerar recomendação: {str(e)}"

    def _get_question_ui_updates(self, question):
        if question['type'] == 'multipla_escolha':
            return (
                question["pergunta"],
                gr.update(choices=question["alternativas"], value=None, interactive=True, visible=True),
                gr.update(visible=False, value="")
            )
        elif question['type'] == 'preencher_lacuna':
            return (
                question["pergunta"],
                gr.update(visible=False, value=None),
                gr.update(visible=True, value="", interactive=True, placeholder="Digite a palavra que falta...")
            )
        return question.get("pergunta", ""), gr.update(visible=False), gr.update(visible=False)

    def start_quiz(self, topic):
        if not topic:
            topic = "cultura e gramática básica"

        
        yield (
            None, 0, 0, 
            gr.update(visible=False), gr.update(visible=True), 
            "", gr.update(), gr.update(), 
            "", gr.update(), gr.update(), 
            " Gerando seu quiz, por favor aguarde..."
        )

        try:
            raw_response = self.quiz_agent.invoke({"topic": topic}).content
            json_match = re.search(r'```json\n({.*?})\n```', raw_response, re.DOTALL)
            json_str = json_match.group(1) if json_match else raw_response
            quiz_data = json.loads(json_str)
            first_question = quiz_data["quiz"][0]
            q_text_update, choices_update, fill_in_update = self._get_question_ui_updates(first_question)

            yield (
                quiz_data, 0, 0,
                gr.update(visible=True), gr.update(visible=False),
                q_text_update, choices_update, fill_in_update,
                "", gr.update(visible=True), gr.update(visible=False), ""
            )
        except Exception as e:
            error_message = f" Desculpe, não consegui gerar o quiz. Tente novamente.\nErro: {str(e)}"
            yield (
                None, 0, 0,
                gr.update(visible=False), gr.update(visible=True),
                "", gr.update(), gr.update(),
                "", gr.update(), gr.update(), error_message
            )

    def submit_answer(self, mc_choice, fill_in_answer, quiz_data, current_question_index, score):
        question_info = quiz_data["quiz"][current_question_index]
        correct_answer = question_info["resposta_correta"]
        user_answer = ""
        if question_info['type'] == 'multipla_escolha': user_answer = mc_choice
        elif question_info['type'] == 'preencher_lacuna': user_answer = fill_in_answer.strip()
        if user_answer and user_answer.lower() == correct_answer.lower():
            score += 1
            feedback = f"<h3>✅ Correto!</h3><p>{question_info['explicacao']}</p>"
        else:
            feedback = f"<h3>❌ Incorreto.</h3><p>A resposta correta é: <b>{correct_answer}</b>.</p><p>{question_info['explicacao']}</p>"
        return score, feedback, gr.update(visible=False), gr.update(visible=True), gr.update(interactive=False), gr.update(interactive=False)
        
    def next_question(self, quiz_data, current_question_index, score):
        current_question_index += 1
        if current_question_index < len(quiz_data["quiz"]):
            next_q = quiz_data["quiz"][current_question_index]
            q_text_update, choices_update, fill_in_update = self._get_question_ui_updates(next_q)
            return (
                current_question_index, q_text_update, choices_update, fill_in_update,
                "", gr.update(visible=True), gr.update(visible=False), 
                gr.update(visible=True), gr.update(visible=False), ""
            )
        else:
            total_questions = len(quiz_data["quiz"])
            summary = f"<h2> Quiz Finalizado!</h2><h3>Sua pontuação: {score} de {total_questions}</h3>"
            return (
                current_question_index, "", gr.update(visible=False), gr.update(visible=False),
                "", gr.update(visible=True), gr.update(visible=False),
                gr.update(visible=False), gr.update(visible=True), summary
            )

    def start_simulation(self, scenario):
        if not scenario:
            yield None, [], gr.update(visible=True), gr.update(visible=False)
            return
        
        initial_history_loading = [{"role": "assistant", "content": " Preparando a simulação, aguarde..."}]
        yield None, initial_history_loading, gr.update(visible=False), gr.update(visible=True)

        try:
            self.roleplay_session_id = str(uuid.uuid4())
            initial_response = self.roleplay_agent.invoke({"input": scenario}, config={"configurable": {"session_id": self.roleplay_session_id}})
            initial_history = [{"role": "assistant", "content": initial_response.content}]
            yield self.roleplay_session_id, initial_history, gr.update(visible=False), gr.update(visible=True)
        except Exception as e:
            error_message = f" Erro ao iniciar simulação: {e}"
            yield None, [{"role": "assistant", "content": error_message}], gr.update(visible=True), gr.update(visible=False)

    def process_roleplay_message(self, message, history, session_id):
        if not message or not session_id:
            yield history, ""
            return
            
        history.append({"role": "user", "content": message})
        history.append({"role": "assistant", "content": " Pensando..."})
        yield history, ""

        try:
            response = self.roleplay_agent.invoke({"input": message}, config={"configurable": {"session_id": session_id}})
            history[-1]["content"] = response.content
            yield history, ""
        except Exception as e:
            error_message = f" Desculpe, ocorreu um erro na simulação: {str(e)}"
            if history:
                history[-1]["content"] = error_message
            else:
                history.append({"role": "user", "content": message})
                history.append({"role": "assistant", "content": error_message})
            yield history, ""

    def end_simulation(self):
        self.roleplay_session_id = None
        return None, [], gr.update(visible=True), gr.update(visible=False), ""

    def update_topics_dropdown(self, level):
        topics = get_topics_for_level(level)
        return gr.Dropdown(choices=topics, value=None, interactive=True)

    def generate_lesson(self, level, topic):
        if not level or not topic:
            yield "Por favor, selecione um nível e um tópico para começar."
            return
        try:
            yield "Gerando sua lição, por favor aguarde..."
            response = self.lessons_agent.invoke({"level": level, "topic": topic}).content
            yield response
        except Exception as e:
            yield f" Desculpe, ocorreu um erro ao gerar a lição: {str(e)}"