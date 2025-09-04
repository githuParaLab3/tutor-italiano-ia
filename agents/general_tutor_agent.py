import os
from dotenv import load_dotenv
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, AIMessage
from langchain_community.chat_message_histories import ChatMessageHistory
from agents.gemini_model import get_gemini_llm
from prompts.general_tutor_prompts import get_general_tutor_prompt

def create_general_tutor_agent():
    llm = get_gemini_llm()
    prompt_template = get_general_tutor_prompt()
    
    chain = ChatPromptTemplate.from_template(prompt_template) | llm

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

store = {}