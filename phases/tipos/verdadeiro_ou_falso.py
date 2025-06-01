# phases/verdadeiro_falso.py
import streamlit as st

def render_verdadeiro_falso(conteudo):
    st.subheader("Verdadeiro ou Falso")

    afirmativa = conteudo.get("afirmativa", "Afirmativa não fornecida.")
    correta = conteudo.get("resposta_correta", True)
    explicacao = conteudo.get("explicacao", "Sem explicação disponível.")

    escolha = st.radio(afirmativa, ["Verdadeiro", "Falso"], key=f"vf_{afirmativa[:10]}")

    if st.button("Responder", key=f"responder_vf_{afirmativa[:10]}"):
        escolha_bool = escolha == "Verdadeiro"
        if escolha_bool == correta:
            st.success("✅ Resposta correta!")
            st.session_state.pontuacao += 1
        else:
            st.error(f"❌ Resposta incorreta. A correta era: **{'Verdadeiro' if correta else 'Falso'}**")
        st.info(f"💡 {explicacao}")
