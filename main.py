#!/usr/bin/env python3
"""
Tutor de Italiano IA - Aplicação Principal
"""

import os
import sys
from dotenv import load_dotenv

load_dotenv()

def check_environment():
    """Verifica se as variáveis de ambiente necessárias estão configuradas."""
    if not os.getenv("GOOGLE_API_KEY"):
        print("Variável de ambiente faltando: GOOGLE_API_KEY")
        print("\nPor favor, configure esta variável no ficheiro .env")
        return False
    
    print("Variáveis de ambiente configuradas corretamente!")
    return True

def main():
    """Função principal que inicia a aplicação."""
    print("🇮🇹 Iniciando o Tutor de Italiano IA...")
    
    if not check_environment():
        sys.exit(1)
    
    try:
        # Atualize esta linha para importar do novo ficheiro
        from ui.main_interface import create_main_interface
        
        print("Carregando a interface...")
        app = create_main_interface()
        
        print("Iniciando o servidor...")
        app.launch(
            server_name="0.0.0.0",
            server_port=7860,
            share=False,
            debug=False
        )
        
    except ImportError as e:
        print(f"Erro de importação: {e}")
        print("Certifique-se de que todas as dependências estão instaladas:")
        print("pip install -r requirements.txt")
        sys.exit(1)
    except Exception as e:
        print(f"Erro inesperado: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()