import streamlit as st

def exibir(fase_dict):
    st.markdown("### Ordene os Passos")
    itens = fase_dict.get("itens", ["Passo 1", "Passo 2", "Passo 3"])
    corretos = sorted(itens)  # Assume ordem alfabética ou lógica básica

    ordem_usuario = st.multiselect("Selecione os itens na ordem correta:", itens, default=[])

    if st.button("Verificar ordem", key=f"botao_ordem_{fase_dict['conceito']}"):
        if ordem_usuario == corretos:
            st.success("✅ Ordem correta!")
        else:
            st.warning(f"⚠️ Ordem incorreta. Esperado: {', '.join(corretos)}")
