import streamlit as st

def exibir(fase_dict):
    st.markdown("### Complete o Texto")
    prompt = fase_dict.get("prompt", "O Transformer é uma arquitetura baseada em ___ que revolucionou o processamento de linguagem natural.")
    resposta_correta = fase_dict.get("resposta", "atenção")

    entrada = st.text_input("Complete a lacuna:", key=f"completar_{fase_dict['conceito']}")

    if st.button("Verificar resposta", key=f"botao_completar_{fase_dict['conceito']}"):
        if entrada.strip().lower() == resposta_correta.lower():
            st.success("✅ Muito bem!")
        else:
            st.error(f"❌ Resposta incorreta. A resposta esperada era: **{resposta_correta}**")
