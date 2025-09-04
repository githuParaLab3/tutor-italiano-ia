from langchain_core.prompts import PromptTemplate
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
from agents.gemini_model import get_gemini_llm
from prompts.roleplay_prompts import get_roleplay_prompt

def create_roleplay_agent():
    llm = get_gemini_llm()
    
    prompt = PromptTemplate(
        input_variables=["history", "input"],
        template=get_roleplay_prompt()
    )
    chain = prompt | llm
    
    global store
    store = {}
    
    def get_session_history(session_id: str) -> ChatMessageHistory:
        if session_id not in store:
            store[session_id] = ChatMessageHistory()
        return store[session_id]
        
    chain_with_history = RunnableWithMessageHistory(
        chain,
        get_session_history,
        input_messages_key="input",
        history_messages_key="history",
    )
    
    return chain_with_history