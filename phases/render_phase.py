from phases.tipos import (
    quiz_multipla_escolha,
    ordenar_passos,
    verdadeiro_ou_falso,
    associacao_termos,
    completar_texto
)

def render_fase(fase_dict):
    tipo = fase_dict["tipo"]

    if tipo == "quiz_multipla_escolha":
        quiz_multipla_escolha.exibir(fase_dict)
    elif tipo == "ordenar_passos":
        ordenar_passos.exibir(fase_dict)
    elif tipo == "verdadeiro_ou_falso":
        verdadeiro_ou_falso.exibir(fase_dict)
    elif tipo == "associacao_termos":
        associacao_termos.exibir(fase_dict)
    elif tipo == "completar_texto":
        completar_texto.exibir(fase_dict)
    else:
        st.warning("Tipo de fase não reconhecido.")
