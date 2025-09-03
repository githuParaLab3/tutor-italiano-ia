from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from agents.gemini_model import get_gemini_llm
from prompts.quiz_prompts import get_quiz_prompt

def create_quiz_agent():
    llm = get_gemini_llm()
    prompt = PromptTemplate.from_template(get_quiz_prompt(quiz_type='{quiz_type}', topic='{topic}'))
    return LLMChain(llm=llm, prompt=prompt)


