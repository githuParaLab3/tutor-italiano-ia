from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from agents.gemini_model import get_gemini_llm
from prompts.general_tutor_prompts import get_general_tutor_prompt

def create_general_tutor_agent():
    llm = get_gemini_llm()
    
    
    prompt = PromptTemplate(
        input_variables=["history", "input"],
        template=get_general_tutor_prompt()
    )
    

    chain = ConversationChain(
        llm=llm,
        prompt=prompt,
        memory=ConversationBufferMemory(human_prefix="Usuário", ai_prefix="Tutor IA"),
        verbose=False 
    )
    return chain