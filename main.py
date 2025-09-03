#!/usr/bin/env python3
"""
Tutor de Italiano IA - Aplicação Principal
==========================================

Este é o ponto de entrada principal para o aplicativo Tutor de Italiano IA.
O aplicativo usa LangChain para a lógica do agente e Gradio para a interface do usuário.

Para executar:
    python main.py

Certifique-se de ter configurado as variáveis de ambiente necessárias no arquivo .env:
    - GOOGLE_API_KEY: Chave da API do Google para o modelo Gemini
    - GOOGLE_CSE_ID: ID do Custom Search Engine do Google (opcional, para pesquisa web)
"""

import os
import sys
from dotenv import load_dotenv

# Carrega as variáveis de ambiente
load_dotenv()

def check_environment():
    """Verifica se as variáveis de ambiente necessárias estão configuradas."""
    required_vars = ["GOOGLE_API_KEY"]
    missing_vars = []
    
    for var in required_vars:
        if not os.getenv(var):
            missing_vars.append(var)
    
    if missing_vars:
        print("❌ Variáveis de ambiente faltando:")
        for var in missing_vars:
            print(f"   - {var}")
        print("\nPor favor, configure essas variáveis no arquivo .env")
        return False
    
    print("✅ Variáveis de ambiente configuradas corretamente!")
    return True

def main():
    """Função principal que inicia a aplicação."""
    print("🇮🇹 Iniciando o Tutor de Italiano IA...")
    
    # Verifica o ambiente
    if not check_environment():
        sys.exit(1)
    
    try:
        # Importa e inicia a interface Gradio
        from ui.gradio_interface import create_gradio_app
        
        print("🚀 Carregando a interface...")
        app = create_gradio_app()
        
        print("🌐 Iniciando o servidor...")
        app.launch(
            server_name="0.0.0.0",
            server_port=7860,
            share=False,
            debug=False
        )
        
    except ImportError as e:
        print(f"❌ Erro de importação: {e}")
        print("Certifique-se de que todas as dependências estão instaladas:")
        print("pip install -r requirements.txt")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

