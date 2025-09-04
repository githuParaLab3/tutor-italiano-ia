from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from agents.gemini_model import get_gemini_llm
from prompts.recommendation_prompts import get_recommendation_prompt

def create_recommendation_agent():
    llm = get_gemini_llm()
    prompt = PromptTemplate.from_template(get_recommendation_prompt(interest='{interest}'))
    return prompt | llm


