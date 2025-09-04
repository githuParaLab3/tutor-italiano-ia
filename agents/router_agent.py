from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from agents.gemini_model import get_gemini_llm

def create_router_agent():
    llm = get_gemini_llm()
    prompt_template = """
Você é um roteador de conversas. Dado o seguinte input do usuário, decida qual das seguintes categorias ele se encaixa melhor:

- 'tutor_geral': Se o usuário estiver fazendo perguntas gerais sobre italiano, pedindo correções, ou apenas conversando em italiano.
- 'traducao': Se o usuário pedir para traduzir algo entre italiano e português.
- 'quiz': Se o usuário pedir um quiz ou teste sobre gramática ou vocabulário.
- 'gramatica': Se o usuário pedir uma explicação sobre um conceito gramatical específico.
- 'recomendacao': Se o usuário pedir sugestões de filmes, séries, livros ou músicas em italiano.
- 'pesquisa': Se o usuário fizer uma pergunta sobre história, geografia, cultura italiana ou qualquer tópico que exija uma resposta mais elaborada que uma simples conversa.

Retorne apenas o nome da categoria. Não adicione nenhuma outra informação.

Input do usuário: {user_input}
Categoria:
"""
    prompt = PromptTemplate.from_template(prompt_template)
    return LLMChain(llm=llm, prompt=prompt)