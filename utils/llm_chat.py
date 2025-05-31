import streamlit as st
import requests

def llm_sidebar_consultation():
    st.sidebar.image("assets/logo.png", use_container_width=True)
    st.sidebar.markdown("---")
    st.sidebar.markdown("🤖 **Tem alguma dúvida?** Pergunte aqui para a LLM!")
    st.sidebar.markdown("_Qwen2.5-7B-Instruct, via Hugging Face_")

    user_question = st.sidebar.text_area("Digite sua dúvida abaixo:", key="hf_chat_user_question")

    if st.sidebar.button("Enviar pergunta", key="hf_chat_submit") and user_question.strip():
        with st.spinner("Consultando a LLM..."):
            try:
                hf_token = st.secrets["HF_TOKEN"]
                headers = {
                    "Authorization": f"Bearer {hf_token}",
                    "Content-Type": "application/json"
                }

                API_URL = "https://router.huggingface.co/together/v1/chat/completions"
                payload = {
                    "model": "Qwen/Qwen2.5-7B-Instruct-Turbo",
                    "messages": [
                        {"role": "user", "content": user_question.strip()}
                    ],
                    "temperature": 0.7,
                    "max_tokens": 300
                }

                response = requests.post(API_URL, headers=headers, json=payload, timeout=30)

                if response.status_code == 200:
                    result = response.json()
                    reply = result["choices"][0]["message"]["content"]
                    st.sidebar.success("📘 Resposta da LLM:")
                    st.sidebar.markdown(f"> {reply.strip()}")
                elif response.status_code == 429:
                    st.sidebar.error("⚠️ Ops, atingimos o limite de requests para o modelo!")
                else:
                    st.sidebar.error("❌ Ocorreu um erro inesperado ao consultar a LLM.")

            except Exception as e:
                st.sidebar.error("❌ Ocorreu um erro técnico ao tentar se conectar à LLM.")

    st.sidebar.markdown("---")

