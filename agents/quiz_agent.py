from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from agents.gemini_model import get_gemini_llm
from prompts.quiz_prompts import get_interactive_quiz_prompt

def create_quiz_agent():
    llm = get_gemini_llm()
    
    template = get_interactive_quiz_prompt()
    
    prompt = PromptTemplate.from_template(template)
    
    return prompt | llm