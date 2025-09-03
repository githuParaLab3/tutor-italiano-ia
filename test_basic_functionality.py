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

def main():
    """Executa todos os testes."""
    print("🚀 Iniciando testes básicos do Tutor de Italiano IA...\n")
    
    imports_ok = test_imports()
    env_ok = test_environment()
    
    print("\n" + "="*50)
    if imports_ok and env_ok:
        print("✅ Todos os testes passaram! O projeto está pronto para uso.")
        print("Execute 'python main.py' para iniciar a aplicação.")
    else:
        print("❌ Alguns testes falharam. Verifique os erros acima.")
    print("="*50)

if __name__ == "__main__":
    main()

