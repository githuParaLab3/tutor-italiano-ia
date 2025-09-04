import gradio as gr

def create_chat_tab(logic_handler): # Adicionado logic_handler
    with gr.TabItem("💬 Chat Inteligente"):
        chatbot = gr.Chatbot(height=500, label="💬 Conversa com seu Tutor Pessoal", avatar_images=("https://cdn-icons-png.flaticon.com/512/3233/3233519.png", "https://cdn-icons-png.flaticon.com/512/4712/4712030.png"), bubble_full_width=False, render_markdown=True)
        audio_output = gr.Audio(label="🎧 Para ouvir, clique em uma mensagem do tutor", interactive=False)
        with gr.Row():
            with gr.Column(scale=4):
                msg = gr.Textbox(placeholder="💭 Pergunte sobre gramática, peça traduções ou apenas converse em italiano...", show_label=False)
            with gr.Column(scale=1):
                send_btn = gr.Button("Enviar 🚀", elem_classes=["button-primary"])
        clear = gr.Button("🗑️ Limpar Chat", elem_classes=["gr-button-secondary"])
    
    return chatbot, msg, send_btn, clear, audio_output