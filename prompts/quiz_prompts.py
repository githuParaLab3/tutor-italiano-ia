def get_quiz_prompt(quiz_type, topic):
    """Mantém o prompt antigo para compatibilidade, se necessário."""
    return f"""
Crie um quiz rápido sobre {topic}. O quiz deve ser do tipo {quiz_type}. 
Se for de múltipla escolha, forneça 4 opções e a resposta correta. 
Se for de preencher lacunas, indique a lacuna com [___].
"""


def get_interactive_quiz_prompt():
    """
    Retorna uma string de template de prompt para o quiz interativo.
    As chaves {{}} no exemplo JSON são escapadas para não serem
    interpretadas pelo Python. A única variável real é {topic}.
    """
    template = """
Você é um especialista em criar quizzes de italiano. 
Sua tarefa é criar um quiz interativo sobre o tópico '{topic}'.
O quiz deve ter exatamente 4 perguntas de múltipla escolha.

Por favor, formate a sua resposta como um objeto JSON VÁLIDO,
seguindo estritamente a estrutura do exemplo abaixo. 
Não adicione nenhum texto ou formatação fora do objeto JSON.

Exemplo de formato:
{{
  "quiz": [
    {{
      "pergunta": "Qual artigo é usado antes da palavra 'scuola'?",
      "alternativas": ["Il", "Lo", "La", "L'"],
      "resposta_correta": "La",
      "explicacao": "'Scuola' é uma palavra feminina que começa com uma consoante, então o artigo correto é 'La'."
    }},
    {{
      "pergunta": "Como se diz 'eu sou' em italiano?",
      "alternativas": ["Io sei", "Io sono", "Io è", "Io siamo"],
      "resposta_correta": "Io sono",
      "explicacao": "A conjugação correta do verbo 'essere' na primeira pessoa do singular é 'sono'."
    }}
  ]
}}
"""
    return template
