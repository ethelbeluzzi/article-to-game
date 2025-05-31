import random
import textwrap

TIPOS_DE_FASE = [
    "quiz_multipla_escolha",
    "ordenar_passos",
    "verdadeiro_ou_falso",
    "associacao_termos",
    "completar_texto"
]

def gerar_trechos(texto, n=5):
    paragrafos = [p.strip() for p in texto.split("\n") if len(p.strip()) > 100]
    if len(paragrafos) < n:
        paragrafos *= (n // len(paragrafos)) + 1
    return random.sample(paragrafos, n)

def gerar_fase(trecho, i):
    conceito = f"Conceito-chave #{i+1}"
    explicacao = f"Este trecho trata de um ponto importante do artigo. Em resumo, ele apresenta um conceito essencial para o entendimento geral do texto."
    tipo = TIPOS_DE_FASE[i % len(TIPOS_DE_FASE)]
    alem_do_artigo = "Este conceito também pode ser observado em contextos contemporâneos, como em sistemas de IA ou mudanças sociais recentes."

    return {
        "tipo": tipo,
        "conceito": conceito,
        "trecho": textwrap.shorten(trecho, width=400, placeholder="..."),
        "explicacao": explicacao,
        "alem_do_artigo": alem_do_artigo
    }

def generate_game_structure(texto):
    fases = []
    trechos = gerar_trechos(texto, 5)
    for i, trecho in enumerate(trechos):
        fase = gerar_fase(trecho, i)
        fases.append(fase)

    return {
        "titulo": "Jogo Gerado a partir de Artigo",
        "resumo": "Este jogo foi criado automaticamente com base em um artigo enviado pelo usuário.",
        "fases": fases
    }
