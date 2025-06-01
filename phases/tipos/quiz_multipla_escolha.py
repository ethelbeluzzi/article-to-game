import streamlit as st

def render_quiz_multipla_escolha(conteudo):
    st.subheader("Quiz de Múltipla Escolha")

    pergunta = conteudo.get("pergunta", "Pergunta não fornecida.")
    opcoes = conteudo.get("opcoes", [])
    correta = conteudo.get("resposta_correta")
    explicacao = conteudo.get("explicacao", "Sem explicação disponível.")

    escolha = st.radio(pergunta, opcoes, key=f"quiz_{pergunta[:10]}")

    if st.button("Responder", key=f"responder_{pergunta[:10]}"):
        if escolha == correta:
            st.success("✅ Resposta correta!")
            st.session_state.pontuacao += 1
        else:
            st.error(f"❌ Resposta incorreta. A correta era: **{correta}**")
        st.info(f"💡 {explicacao}")
