
def get_translation_prompt(text_to_translate, target_language):
    return f"""
Traduza o seguinte texto para {target_language}. Se o texto for em italiano, traduza para português. Se for em português, traduza para italiano.

Texto: {text_to_translate}
"""


