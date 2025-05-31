import streamlit as st

def exibir(fase_dict):
    st.markdown("### Associe os Termos")
    pares = fase_dict.get("pares", {"Transformers": "Arquitetura de IA", "Embedding": "Representação vetorial"})

    for termo, definicao_correta in pares.items():
        resposta = st.selectbox(
            f"O que melhor descreve **{termo}**?",
            list(set(pares.values())),
            key=f"assoc_{termo}"
        )
        if resposta == definicao_correta:
            st.success(f"✅ {termo} → {resposta}")
        else:
            st.error(f"❌ {termo} → {resposta} (Correto: {definicao_correta})")
