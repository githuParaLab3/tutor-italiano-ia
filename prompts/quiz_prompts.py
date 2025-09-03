
def get_quiz_prompt(quiz_type, topic):
    return f"""
Crie um quiz rápido sobre {topic}. O quiz deve ser do tipo {quiz_type}. Se for de múltipla escolha, forneça 4 opções e a resposta correta. Se for de preencher lacunas, indique a lacuna com [___].
"""


