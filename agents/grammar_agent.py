from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from agents.gemini_model import get_gemini_llm
from prompts.grammar_prompts import get_grammar_lesson_prompt

def create_grammar_agent():
    llm = get_gemini_llm()
    prompt = PromptTemplate.from_template(get_grammar_lesson_prompt(concept='{concept}'))
    return LLMChain(llm=llm, prompt=prompt)


