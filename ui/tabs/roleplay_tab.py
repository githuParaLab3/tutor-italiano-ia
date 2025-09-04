import gradio as gr

def create_roleplay_tab(logic_handler): 
    with gr.TabItem("Simulação (Role-play)"):
        roleplay_agent_state = gr.State()
        with gr.Column(visible=True) as roleplay_setup_wrapper:
            gr.Markdown("### <span class='tool-heading'>Prática de Conversação</span>")
            rp_scenario_input = gr.Textbox(placeholder="Ex: Em um restaurante pedindo uma pizza...", label="Descreva o cenário que você quer praticar:")
            rp_start_btn = gr.Button("Iniciar Simulação", elem_classes=["button-primary"])
        with gr.Column(visible=False) as roleplay_chat_wrapper:
            rp_chatbot = gr.Chatbot(height=450, label="Simulação em Andamento", avatar_images=("https://cdn-icons-png.flaticon.com/512/3233/3233519.png", "https://cdn-icons-png.flaticon.com/512/1211/1211019.png"), bubble_full_width=False, render_markdown=True)
            rp_audio_output = gr.Audio(label="Para ouvir, clique em uma mensagem do ator", interactive=False)
            with gr.Row():
                with gr.Column(scale=4):
                    rp_msg = gr.Textbox(placeholder="Digite sua resposta em italiano...", show_label=False)
                with gr.Column(scale=1):
                    rp_send_btn = gr.Button("Enviar", elem_classes=["button-primary"])
            rp_end_btn = gr.Button("Terminar Simulação", elem_classes=["gr-button-secondary"])

    return roleplay_agent_state, roleplay_setup_wrapper, rp_scenario_input, rp_start_btn, roleplay_chat_wrapper, rp_chatbot, rp_audio_output, rp_msg, rp_send_btn, rp_end_btn