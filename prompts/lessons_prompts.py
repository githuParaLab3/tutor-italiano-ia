def get_lesson_prompt(level, topic):
    """
    Gera um prompt para criar uma lição estruturada sobre um tópico específico.
    """
    return f"""
Você é um professor de italiano experiente criando material didático. Sua tarefa é desenvolver uma mini-lição completa sobre o tópico "{topic}" para um aluno do nível "{level}".

A lição deve ser clara, concisa e prática. Siga estritamente esta estrutura, usando Markdown para formatação:

### Lição: {topic} (Nível: {level})

**1. Objetivo da Lição:**
(Descreva em uma frase o que o aluno será capaz de fazer após completar esta lição.)

**2. Explicação (Teoria):**
(Explique o conceito principal de forma simples e direta. Se for gramática, explique as regras. Se for vocabulário, apresente as palavras com suas traduções.)

**3. Exemplos em Contexto:**
(Forneça de 3 a 5 frases de exemplo em italiano que usem o conceito ou vocabulário da lição. Inclua a tradução em português para cada exemplo.)

**4. Dica Cultural (se aplicável):**
(Se houver alguma nuance cultural ou uma dica prática relacionada ao tópico, adicione-a aqui. Por exemplo, ao ensinar sobre pedidos em um café, mencione que o "caffè" na Itália é um expresso.)

**5. Mini-Exercício:**
(Crie um exercício prático com 2 ou 3 perguntas de "preencher lacunas" ou "traduza esta frase" para que o aluno possa aplicar o que aprendeu. Forneça as respostas corretas no final, sob um título "Respostas".)

---
"""