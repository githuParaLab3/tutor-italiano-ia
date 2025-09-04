from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from agents.gemini_model import get_gemini_llm
from prompts.translation_prompts import get_translation_prompt

def create_translation_agent():
    llm = get_gemini_llm()
    prompt = PromptTemplate.from_template(get_translation_prompt(text_to_translate='{text}', target_language='{language}'))
    return prompt | llm


