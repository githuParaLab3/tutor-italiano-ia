import gradio as gr

def create_quick_tools_tab(logic_handler):
    with gr.TabItem("Ferramentas Rápidas"):
        quiz_data_state = gr.State()
        quiz_score_state = gr.State()
        quiz_question_index_state = gr.State()

        with gr.Row():
            with gr.Column(elem_classes=["quick-tools-section"]):
                gr.Markdown("### <span class='tool-heading'>Tradutor Profissional</span>")
                translation_input = gr.Textbox(placeholder="Digite ou cole o texto...", label="Texto para Tradução", lines=3)
                translation_output = gr.Markdown(label="Resultado")
                with gr.Row():
                    translate_btn = gr.Button("Traduzir Agora", elem_classes=["button-primary"])
                    translate_clear_btn = gr.Button("Limpar", elem_classes=["gr-button-secondary"])
            with gr.Column(elem_classes=["quick-tools-section"]):
                gr.Markdown("### <span class='tool-heading'>Quiz Interativo</span>")
                with gr.Column(visible=True) as start_quiz_wrapper:
                    quiz_topic_input = gr.Textbox(placeholder="Ex: verbos, artigos, preposições...", label="Tópico do Quiz (opcional)")
                    with gr.Row():
                        quiz_btn = gr.Button("Gerar Novo Quiz", elem_classes=["button-primary"])
                        quiz_clear_btn = gr.Button("Limpar Quiz", elem_classes=["gr-button-secondary"])
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
                gr.Markdown("### <span class='tool-heading'>Recomendações IA</span>")
                interest_input = gr.Textbox(placeholder="Ex: cinema, música, culinária...", label="Seus Interesses")
                recommendation_output = gr.Markdown(label="Recomendações")
                with gr.Row():
                    recommend_btn = gr.Button("✨ Descobrir Conteúdo", elem_classes=["button-primary"])
                    recommend_clear_btn = gr.Button("Limpar", elem_classes=["gr-button-secondary"])

    components = {
        "states": [quiz_data_state, quiz_score_state, quiz_question_index_state],
        "translation": [translation_input, translation_output, translate_btn, translate_clear_btn],
        "quiz_main": [start_quiz_wrapper, quiz_container, quiz_topic_input, quiz_btn, quiz_clear_btn, quiz_summary_text],
        "quiz_elements": [quiz_question_text, quiz_choices, quiz_fill_in_input, quiz_feedback_text, quiz_submit_button, quiz_next_button],
        "recommendation": [interest_input, recommendation_output, recommend_btn, recommend_clear_btn]
    }
    return components