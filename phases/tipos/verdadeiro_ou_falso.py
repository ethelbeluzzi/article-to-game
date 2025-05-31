import streamlit as st

def exibir(fase_dict):
    st.markdown("### Verdadeiro ou Falso")
    afirmacao = fase_dict.get("afirmacao", "Esta afirmação é verdadeira?")
    correta = fase_dict.get("correta", "Verdadeiro")

    escolha = st.radio(afirmacao, ["Verdadeiro", "Falso"], key=f"vf_{fase_dict['conceito']}")

    if st.button("Verificar", key=f"botao_vf_{fase_dict['conceito']}"):
        if escolha == correta:
            st.success("✅ Isso mesmo!")
        else:
            st.error(f"❌ Resposta incorreta. O correto era: **{correta}**")
