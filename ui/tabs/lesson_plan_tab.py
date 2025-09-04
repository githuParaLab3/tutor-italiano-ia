import gradio as gr
from core.curriculum import get_levels

def create_lesson_plan_tab(logic_handler): 
    with gr.TabItem("Plano de Estudos"):
        gr.Markdown("### <span class='tool-heading'>Seu Roteiro de Aprendizado</span>")
        with gr.Row():
            with gr.Column(scale=1):
                level_dropdown = gr.Dropdown(label="1. Escolha seu Nível", choices=get_levels(), value=None)
            with gr.Column(scale=2):
                topic_dropdown = gr.Dropdown(label="2. Escolha a Lição", interactive=False)
        with gr.Row():
            lesson_btn = gr.Button("Gerar Lição", elem_classes=["button-primary"])
            lesson_clear_btn = gr.Button("Limpar", elem_classes=["gr-button-secondary"])
        lesson_output = gr.Markdown("Sua lição aparecerá aqui...")
        
    return level_dropdown, topic_dropdown, lesson_btn, lesson_clear_btn, lesson_output