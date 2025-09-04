def get_interactive_quiz_prompt():
    """
    Retorna uma string de template de prompt para o quiz interativo,
    capaz de gerar múltiplos tipos de perguntas.
    """
    template = """
Você é um especialista em criar quizzes de italiano. 
Sua tarefa é criar um quiz interativo sobre o tópico '{topic}'.
O quiz deve ter exatamente 4 perguntas, misturando os tipos "múltipla escolha" e "preencher lacunas".

Por favor, formate a sua resposta como um objeto JSON VÁLIDO.
Siga estritamente a estrutura do exemplo abaixo, prestando atenção ao campo "type".

- Para "multipla_escolha", a pergunta deve ter "alternativas" e "resposta_correta".
- Para "preencher_lacuna", a pergunta deve conter "[___]" e a "resposta_correta" deve ser a palavra que preenche a lacuna.

Exemplo de formato:
{{
  "quiz": [
    {{
      "type": "multipla_escolha",
      "pergunta": "Qual artigo é usado antes da palavra 'scuola'?",
      "alternativas": ["Il", "Lo", "La", "L'"],
      "resposta_correta": "La",
      "explicacao": "'Scuola' é uma palavra feminina que começa com uma consoante, então o artigo correto é 'La'."
    }},
    {{
      "type": "preencher_lacuna",
      "pergunta": "Io [___] un caffè, per favore.",
      "resposta_correta": "vorrei",
      "explicacao": "'Vorrei' é a forma condicional do verbo 'volere' (querer) e é a maneira mais educada de pedir algo."
    }},
    {{
      "type": "multipla_escolha",
      "pergunta": "Como se diz 'eu sou' em italiano?",
      "alternativas": ["Io sei", "Io sono", "Io è", "Io siamo"],
      "resposta_correta": "Io sono",
      "explicacao": "A conjugação correta do verbo 'essere' na primeira pessoa do singular é 'sono'."
    }}
  ]
}}
"""
    return template