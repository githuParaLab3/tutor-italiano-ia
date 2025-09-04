import gradio as gr
from .logic_handler import LogicHandler
from .tabs.chat_tab import create_chat_tab
from .tabs.lesson_plan_tab import create_lesson_plan_tab
from .tabs.roleplay_tab import create_roleplay_tab
from .tabs.quick_tools_tab import create_quick_tools_tab
from .styles import custom_css

def create_main_interface():
    """
    Cria e monta a interface principal do Gradio, unindo todas as abas.
    """
    logic_handler = LogicHandler()

    with gr.Blocks(title="🇮🇹 Tutor de Italiano IA", theme=gr.themes.Soft(primary_hue="indigo", secondary_hue="blue", neutral_hue="slate"), css=custom_css) as interface:
        
        gr.Markdown("# <span class='main-heading'>🇮🇹 Tutor de Italiano IA</span>")
        gr.Markdown("<span class='sub-heading'>Sua jornada personalizada para dominar o italiano com inteligência artificial</span>")

        with gr.Tabs(elem_classes=["tabs"]):
            
            chatbot, msg, send_btn, clear, audio_output = create_chat_tab(logic_handler)
            level_dropdown, topic_dropdown, lesson_btn, lesson_clear_btn, lesson_output = create_lesson_plan_tab(logic_handler)
            rp_state, rp_setup, rp_scenario, rp_start, rp_chat, rp_chatbot, rp_audio, rp_msg, rp_send, rp_end = create_roleplay_tab(logic_handler)
            tools_cmps = create_quick_tools_tab(logic_handler)

        
    
        msg.submit(logic_handler.process_message, [msg, chatbot], [chatbot, msg])
        send_btn.click(logic_handler.process_message, [msg, chatbot], [chatbot, msg])
        clear.click(lambda: (None, None), None, [chatbot, audio_output], queue=False)
        chatbot.select(logic_handler.generate_audio_from_selection, None, audio_output)

       
        level_dropdown.change(fn=logic_handler.update_topics_dropdown, inputs=level_dropdown, outputs=topic_dropdown)
        lesson_btn.click(fn=logic_handler.generate_lesson, inputs=[level_dropdown, topic_dropdown], outputs=lesson_output)
        lesson_clear_btn.click(lambda: (gr.update(value=None), gr.update(choices=[], value=None), gr.update(value="")), None, [level_dropdown, topic_dropdown, lesson_output], queue=False)
        

        rp_start.click(logic_handler.start_simulation, inputs=[rp_scenario], outputs=[rp_state, rp_chatbot, rp_setup, rp_chat])
        rp_msg.submit(logic_handler.process_roleplay_message, [rp_msg, rp_chatbot, rp_state], [rp_chatbot, rp_msg])
        rp_send.click(logic_handler.process_roleplay_message, [rp_msg, rp_chatbot, rp_state], [rp_chatbot, rp_msg])
        rp_chatbot.select(logic_handler.generate_audio_from_selection, None, rp_audio)
        rp_end.click(logic_handler.end_simulation, [], [rp_state, rp_chatbot, rp_setup, rp_chat, rp_scenario])

 
        tools_cmps["translation"][2].click(logic_handler.quick_translation, tools_cmps["translation"][0], tools_cmps["translation"][1])
        tools_cmps["translation"][3].click(lambda: (gr.update(value=""), gr.update(value="")), None, [tools_cmps["translation"][0], tools_cmps["translation"][1]], queue=False)
        
        tools_cmps["recommendation"][2].click(logic_handler.quick_recommendation, tools_cmps["recommendation"][0], tools_cmps["recommendation"][1])
        tools_cmps["recommendation"][3].click(lambda: (gr.update(value=""), gr.update(value="")), None, [tools_cmps["recommendation"][0], tools_cmps["recommendation"][1]], queue=False)
        
        quiz_data, quiz_score, quiz_idx = tools_cmps["states"]
        start_wrap, q_container, topic_in, quiz_btn, quiz_clear_btn, summary_txt = tools_cmps["quiz_main"]
        q_text, q_choices, q_fill_in, q_feedback, q_submit, q_next = tools_cmps["quiz_elements"]
        
        quiz_outputs = [quiz_data, quiz_score, quiz_idx, q_container, start_wrap, q_text, q_choices, q_fill_in, q_feedback, q_submit, q_next, summary_txt]
        quiz_btn.click(logic_handler.start_quiz, inputs=[topic_in], outputs=quiz_outputs)
        quiz_clear_btn.click(lambda: (None, 0, 0, gr.update(visible=False), gr.update(visible=True), "", gr.update(visible=False, choices=None), gr.update(visible=False, value=""), "", gr.update(visible=True), gr.update(visible=False), ""), None, quiz_outputs, queue=False)
        
        submit_outputs = [quiz_score, q_feedback, q_submit, q_next, q_choices, q_fill_in]
        q_submit.click(logic_handler.submit_answer, inputs=[q_choices, q_fill_in, quiz_data, quiz_idx, quiz_score], outputs=submit_outputs)
        
        next_q_outputs = [quiz_idx, q_text, q_choices, q_fill_in, q_feedback, q_submit, q_next, q_container, start_wrap, summary_txt]
        q_next.click(logic_handler.next_question, inputs=[quiz_data, quiz_idx, quiz_score], outputs=next_q_outputs)

    return interface