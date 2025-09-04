#!/usr/bin/env python3
import os
import sys
import json
import re
import uuid
from dotenv import load_dotenv

load_dotenv()

def test_imports():
    print("🧪 Testando importações...")
    modules_to_test = [
        "agents.gemini_model",
        "agents.general_tutor_agent",
        "agents.translation_agent",
        "agents.quiz_agent",
        "agents.grammar_agent",
        "agents.recommendation_agent",
        "agents.router_agent",
        "agents.roleplay_agent",
        "agents.lessons_agent",
        "ui.logic_handler",
        "ui.main_interface"
    ]
    all_ok = True
    for module_name in modules_to_test:
        try:
            __import__(module_name)
            print(f"✅ {module_name} importado com sucesso")
        except ImportError as e:
            print(f"❌ Erro ao importar {module_name}: {e}")
            all_ok = False
    return all_ok

def test_environment():
    print("\n🔧 Testando variáveis de ambiente...")
    google_api_key = os.getenv("GOOGLE_API_KEY")
    if google_api_key:
        print("✅ GOOGLE_API_KEY configurada")
        return True
    else:
        print("❌ GOOGLE_API_KEY não configurada")
        print("   Crie um arquivo .env com sua chave da API do Google")
        return False

def test_router_agent(logic_handler):
    print("\n🗺️ Testando o roteador de agentes...")
    try:
        inputs = {
            "Traduza 'hello' para italiano": "traducao",
            "Me dê um quiz sobre verbos": "quiz",
            "O que é o 'congiuntivo' em italiano?": "gramatica",
            "Recomende filmes italianos para aprender a língua": "recomendacao",
            "Qual a capital da Itália?": "pesquisa",
            "Vamos simular uma conversa em um café": "roleplay",
            "Ciao, come stai?": "tutor_geral"
        }
        all_ok = True
        for user_input, expected_route in inputs.items():
            route = logic_handler.router_agent.invoke({"user_input": user_input}).content.strip().lower()
            if route == expected_route:
                print(f"✅ Input '{user_input[:20]}...' roteou para '{route}' (Esperado: '{expected_route}')")
            else:
                print(f"❌ Input '{user_input[:20]}...' roteou para '{route}' (Esperado: '{expected_route}')")
                all_ok = False
        return all_ok
    except Exception as e:
        print(f"❌ Erro durante o teste do roteador: {e}")
        return False

def test_general_tutor_and_memory(logic_handler):
    print("\n🧠 Testando a memória do tutor geral...")
    try:
        session_id = str(uuid.uuid4())
        input1 = "Ciao! Il mio nome è Marco."
        input2 = "Qual è il mio nome?"
        logic_handler.general_tutor_chain.invoke(
            {"input": input1},
            config={"configurable": {"session_id": session_id}}
        ).content
        response2 = logic_handler.general_tutor_chain.invoke(
            {"input": input2},
            config={"configurable": {"session_id": session_id}}
        ).content
        if "marco" in response2.lower():
            print(f"✅ Teste de memória passou! O agente lembrou o nome: '{response2}'")
            return True
        else:
            print(f"❌ Teste de memória falhou. O agente não lembrou o nome. Resposta: '{response2}'")
            return False
    except Exception as e:
        print(f"❌ Erro durante o teste de memória: {e}")
        return False

def test_quick_translation(logic_handler):
    print("\n📚 Testando a tradução rápida...")
    try:
        text_to_translate = "Olá, meu nome é João."
        translator_gen = logic_handler.quick_translation(text_to_translate)
        response = None
        for chunk in translator_gen:
            response = chunk
        translation_match = re.search(r'\*\*1\. Tradução Direta:\*\*\n([\s\S]*?)\n\n', response)
        if translation_match:
            translated_text = translation_match.group(1).strip()
            if "ciao, il mio nome è joão." in translated_text.lower() or "ciao! il mio nome è joão." or "Ciao, mi chiamo João." in translated_text.lower():
                print(f"✅ Tradução rápida funcionou. Resposta: '{translated_text[:50]}...'")
                return True
            else:
                print(f"❌ Tradução rápida falhou. Resposta inesperada: '{translated_text}'")
                return False
        else:
            print(f"❌ Tradução rápida falhou. Não foi possível encontrar a seção 'Tradução Direta'. Resposta completa: '{response}'")
            return False
    except Exception as e:
        print(f"❌ Erro durante o teste de tradução: {e}")
        return False

def test_quiz_generation(logic_handler):
    print("\n📝 Testando a geração de quiz...")
    try:
        quiz_gen = logic_handler.start_quiz("gramática básica")
        *_, final_output = quiz_gen
        quiz_data, _, _, _, _, _, _, _, _, _, _, _ = final_output
        if quiz_data and "quiz" in quiz_data and len(quiz_data["quiz"]) == 4:
            print("✅ Geração de quiz funcionou. Quiz tem 4 perguntas.")
            first_q = quiz_data["quiz"][0]
            if "pergunta" in first_q and "explicacao" in first_q:
                print("✅ Estrutura da primeira pergunta validada.")
                return True
            else:
                print("❌ Estrutura da pergunta do quiz é inválida.")
                return False
        else:
            print(f"❌ Geração de quiz falhou. Dados inválidos: {quiz_data}")
            return False
    except Exception as e:
        print(f"❌ Erro durante o teste de quiz: {e}")
        return False

def test_lessons_generation(logic_handler):
    print("\n📖 Testando a geração de lições...")
    try:
        lesson_gen = logic_handler.generate_lesson("A1 (Iniciante)", "Verbo Essere (Ser/Estar)")
        _ = next(lesson_gen)
        response = next(lesson_gen)
        if "### Lição: Verbo Essere (Ser/Estar)" in response and "**1. Objetivo da Lição:**" in response:
            print("✅ Geração de lição funcionou. Resposta contém a estrutura esperada.")
            return True
        else:
            print(f"❌ Geração de lição falhou. Estrutura inesperada: '{response[:100]}...'")
            return False
    except Exception as e:
        print(f"❌ Erro durante o teste de lições: {e}")
        return False

def main():
    print("🚀 Iniciando testes completos do Tutor de Italiano IA...\n")
    imports_ok = test_imports()
    env_ok = test_environment()
    if not (imports_ok and env_ok):
        print("\n" + "="*50)
        print("❌ Alguns testes essenciais falharam. Verifique os erros acima.")
        print("="*50)
        sys.exit(1)
    try:
        from ui.logic_handler import LogicHandler
        logic_handler = LogicHandler()
    except Exception as e:
        print(f"❌ Não foi possível inicializar o LogicHandler: {e}")
        sys.exit(1)
    router_ok = test_router_agent(logic_handler)
    memory_ok = test_general_tutor_and_memory(logic_handler)
    translation_ok = test_quick_translation(logic_handler)
    quiz_ok = test_quiz_generation(logic_handler)
    lessons_ok = test_lessons_generation(logic_handler)
    print("\n" + "="*50)
    if all([imports_ok, env_ok, router_ok, memory_ok, translation_ok, quiz_ok, lessons_ok]):
        print("✅ Todos os testes passaram! O projeto está pronto para uso.")
        print("Execute 'python main.py' para iniciar a aplicação.")
    else:
        print("❌ Alguns testes falharam. Verifique os erros acima.")
    print("="*50)

if __name__ == "__main__":
    main()