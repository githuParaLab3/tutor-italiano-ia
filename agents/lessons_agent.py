# agents/lessons_agent.py

from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from agents.gemini_model import get_gemini_llm
from prompts.lessons_prompts import get_lesson_prompt

def create_lessons_agent():
    """
    Cria um agente especializado em gerar lições estruturadas.
    """
    llm = get_gemini_llm()

    prompt_template = get_lesson_prompt(level='{level}', topic='{topic}')
    
    prompt = PromptTemplate.from_template(prompt_template)
    
    return LLMChain(llm=llm, prompt=prompt)