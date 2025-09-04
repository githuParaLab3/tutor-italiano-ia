from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from agents.gemini_model import get_gemini_llm
from prompts.roleplay_prompts import get_roleplay_prompt

def create_roleplay_agent():
    """
    Cria um agente de conversação especializado em simulações (role-playing).
    """
    llm = get_gemini_llm()
    
    prompt = PromptTemplate(
        input_variables=["history", "input"],
        template=get_roleplay_prompt()
    )
    
    # Usamos uma memória separada para cada simulação
    memory = ConversationBufferMemory(human_prefix="Usuário", ai_prefix="Você")
    
    chain = ConversationChain(
        llm=llm,
        prompt=prompt,
        memory=memory,
        verbose=False
    )
    return chain