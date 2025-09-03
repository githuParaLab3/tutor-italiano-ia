from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from agents.gemini_model import get_gemini_llm
from prompts.general_tutor_prompts import get_general_tutor_prompt

def create_general_tutor_agent():
    llm = get_gemini_llm()
    prompt = PromptTemplate.from_template(get_general_tutor_prompt() + "\n\n{text}")
    return LLMChain(llm=llm, prompt=prompt)


