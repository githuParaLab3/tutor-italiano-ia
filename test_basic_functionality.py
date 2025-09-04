#!/usr/bin/env python3
"""
Script de teste básico para verificar se os componentes estão funcionando.
"""

import os
from dotenv import load_dotenv

load_dotenv()

def test_imports():
    """Testa se todos os módulos podem ser importados."""
    print("🧪 Testando importações...")
    
    try:
        from agents.gemini_model import get_gemini_llm
        print("✅ agents.gemini_model importado com sucesso")
    except Exception as e:
        print(f"❌ Erro ao importar agents.gemini_model: {e}")
        return False
    
    try:
        from agents.general_tutor_agent import create_general_tutor_agent
        print("✅ agents.general_tutor_agent importado com sucesso")
    except Exception as e:
        print(f"❌ Erro ao importar agents.general_tutor_agent: {e}")
        return False
    
    try:
        from ui.gradio_interface import create_gradio_app
        print("✅ ui.gradio_interface importado com sucesso")
    except Exception as e:
        print(f"❌ Erro ao importar ui.gradio_interface: {e}")
        return False
    
    return True

def test_environment():
    """Testa se as variáveis de ambiente estão configuradas."""
    print("\n🔧 Testando variáveis de ambiente...")
    
    google_api_key = os.getenv("GOOGLE_API_KEY")
    if google_api_key:
        print("✅ GOOGLE_API_KEY configurada")
        return True
    else:
        print("❌ GOOGLE_API_KEY não configurada")
        print("   Crie um arquivo .env com sua chave da API do Google")
        return False

def test_conversation_memory():
    """Testa a nova funcionalidade de memória do agente de conversação."""
    print("\n🧠 Testando a memória da conversação...")
    try:
        from agents.general_tutor_agent import create_general_tutor_agent
        
        # Cria uma nova instância do agente para o teste
        tutor_agent = create_general_tutor_agent()
        
        # Simula os inputs da conversa
        input1 = "Ciao! Il mio nome è Marco."
        input2 = "Qual è il mio nome?"
        
        # Executa a cadeia de conversação
        response1 = tutor_agent.predict(input=input1)
        print(f"   - Input 1: '{input1}'")
        print(f"   - Resposta do Tutor 1: '{response1[:50]}...'") # Mostra apenas o início
        
        response2 = tutor_agent.predict(input=input2)
        print(f"   - Input 2: '{input2}'")
        print(f"   - Resposta do Tutor 2: '{response2}'")
        
        # Verifica se a resposta contém a informação memorizada
        if "marco" in response2.lower():
            print("✅ Teste de memória passou! O agente lembrou o nome.")
            return True
        else:
            print("❌ Teste de memória falhou. O agente não lembrou o nome.")
            return False
            
    except Exception as e:
        print(f"❌ Erro durante o teste de memória: {e}")
        return False

def main():
    """Executa todos os testes."""
    print("🚀 Iniciando testes básicos do Tutor de Italiano IA...\n")
    
    imports_ok = test_imports()
    env_ok = test_environment()
    memory_ok = False
    if imports_ok and env_ok:
        memory_ok = test_conversation_memory()
    
    print("\n" + "="*50)
    if imports_ok and env_ok and memory_ok:
        print("✅ Todos os testes passaram! O projeto está pronto para uso.")
        print("Execute 'python main.py' para iniciar a aplicação.")
    else:
        print("❌ Alguns testes falharam. Verifique os erros acima.")
    print("="*50)

if __name__ == "__main__":
    main()