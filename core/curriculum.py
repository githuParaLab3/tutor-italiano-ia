# core/curriculum.py

"""
Define a estrutura do currículo de italiano, organizado por níveis do CEFR (A1-C2).
Cada tópico pode ser usado para gerar uma lição detalhada.
"""

CURRICULUM = {
    "A1 (Iniciante)": [
        "Alfabeto e Pronúncia",
        "Saudações e Apresentações Formais e Informais",
        "Artigos Definidos e Indefinidos (Il, La, Un, Una)",
        "Verbo Essere (Ser/Estar)",
        "Verbo Avere (Ter)",
        "Substantivos: Gênero e Número",
        "Adjetivos: Concordância Básica",
        "Números de 0 a 100",
        "Fazer um pedido em um café ou bar",
        "Falar sobre a família e profissões",
        "Perguntas básicas (Chi?, Cosa?, Dove?, Quando?)",
    ],
    "A2 (Básico)": [
        "Verbos Regulares no Presente (-are, -ere, -ire)",
        "Principais Verbos Irregulares no Presente (Andare, Fare, Potere, Dovere, Volere)",
        "Preposições Simples (di, a, da, in, con, su, per, tra, fra)",
        "Preposições Articuladas (nel, sulla, dai, etc.)",
        "Passato Prossimo: Verbos com 'Avere'",
        "Passato Prossimo: Verbos com 'Essere' e o Acordo do Particípio",
        "Adjetivos Possessivos (Mio, Tuo, Suo...)",
        "Vocabulário de Comida e Restaurante",
        "Pedir e dar informações na rua",
        "Descrever pessoas, lugares e rotinas diárias",
        "O partitivo (del, della...)",
    ],
    "B1 (Intermediário)": [
        "Imperfetto: Uso e Formação",
        "Contraste entre Passato Prossimo e Imperfetto",
        "Futuro Semplice (Futuro Simples)",
        "Pronomes Diretos (lo, la, li, le)",
        "Pronomes Indiretos (mi, ti, gli, le)",
        "A partícula 'ne'",
        "A partícula 'ci' (locativo e pronominal)",
        "Verbos Reflexivos (lavarsi, svegliarsi)",
        "Comparativos e Superlativos",
        "Expressar opiniões, concordar e discordar",
        "Falar sobre planos futuros e hipóteses simples",
    ],
    "B2 (Intermediário Avançado)": [
        "Condizionale Semplice e Composto (Condicional)",
        "Congiuntivo Presente e Passato (Subjuntivo)",
        "Uso do Subjuntivo em Orações Subordinadas",
        "Pronomes Combinados (me lo, te la, glielo...)",
        "Discorso Indiretto (Discurso Indireto) e a Concordância dos Tempos",
        "A Forma Passiva",
        "Período Hipotético (da realidade e da possibilidade)",
        "Vocabulário sobre atualidades, trabalho e meio ambiente",
        "Argumentar e defender um ponto de vista",
    ],
    "C1 (Avançado)": [
        "Congiuntivo Imperfetto e Trapassato (Subjuntivo)",
        "Período Hipotético da Irrealidade",
        "Formas Implícitas (Gerundio, Infinito e Participio)",
        "Conectivos Textuais Complexos (affinché, benché, purché)",
        "Pronomes Relativos Compostos (il quale, cui)",
        "Trapassato Remoto e seu uso literário",
        "Registros Linguísticos (formal, informal, burocrático)",
        "Análise de textos complexos (artigos, ensaios)",
        "Expressões idiomáticas e gírias regionais",
    ],
    "C2 (Proficiente)": [
        "Revisão e Domínio de Todas as Estruturas Gramaticais",
        "Análise Estilística e Figuras de Linguagem",
        "Uso de Formas Verbais Raras e Arcaicas",
        "Compreensão de Variações Dialetais",
        "Produção de Textos Acadêmicos e Profissionais",
        "Técnicas de Resumo e Reformulação de Textos",
        "Debate sobre temas abstratos e filosóficos",
        "Nuances e Sutilezas da Linguagem",
        "Análise da história da língua italiana",
    ]
}

def get_levels():
    """Retorna uma lista dos níveis disponíveis."""
    return list(CURRICULUM.keys())

def get_topics_for_level(level):
    """Retorna la lista de tópicos para um determinado nível."""
    return CURRICULUM.get(level, [])