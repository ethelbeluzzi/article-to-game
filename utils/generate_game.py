# generate_game.py

def validate_fase(fase):
    tipo = fase.get("tipo")
    conteudo = fase.get("conteudo")

    if tipo == "quiz_multipla_escolha":
        if not all(k in conteudo for k in ["pergunta", "alternativas", "correta"]):
            return False
        if len(conteudo["alternativas"]) != 4:
            return False

    elif tipo == "verdadeiro_ou_falso":
        if not all(k in conteudo for k in ["afirmacao", "correta"]):
            return False
        if conteudo["correta"] not in ["Verdadeiro", "Falso"]:
            return False

    elif tipo == "completar_texto":
        if not all(k in conteudo for k in ["texto_incompleto", "resposta"]):
            return False

    else:
        return False

    return True
