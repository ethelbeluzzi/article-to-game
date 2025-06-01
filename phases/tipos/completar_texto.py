import streamlit as st

def render_completar_texto(conteudo):
    st.subheader("Complete o Texto")

    enunciado = conteudo.get("enunciado", "Texto com lacuna não fornecido.")
    opcoes = conteudo.get("opcoes", [])
    correta = conteudo.get("resposta_correta", "")
    explicacao = conteudo.get("explicacao", "Sem explicação disponível.")

    resposta = st.radio(enunciado, opcoes, key=f"ct_{enunciado[:10]}")

    if st.button("Responder", key=f"responder_ct_{enunciado[:10]}"):
        if resposta == correta:
            st.success("✅ Resposta correta!")
            st.session_state.pontuacao += 1
        else:
            st.error(f"❌ Resposta incorreta. A correta era: **{correta}**")
        st.info(f"💡 {explicacao}")
