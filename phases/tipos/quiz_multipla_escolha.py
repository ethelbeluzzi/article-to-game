import streamlit as st

def exibir(fase_dict):
    st.markdown("### Quiz de Múltipla Escolha")
    alternativas = fase_dict.get("alternativas", ["A", "B", "C", "D"])
    correta = fase_dict.get("correta", alternativas[0])
    pergunta = fase_dict.get("pergunta", "Escolha a opção correta:")

    escolha = st.radio(pergunta, alternativas, key=f"quiz_{fase_dict['conceito']}")

    if st.button("Verificar resposta", key=f"botao_quiz_{fase_dict['conceito']}"):
        if escolha == correta:
            st.success("✅ Resposta correta!")
        else:
            st.error(f"❌ Resposta incorreta. A correta era: **{correta}**")
