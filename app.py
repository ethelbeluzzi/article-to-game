import streamlit as st
import uuid
from utils.extract_text import extract_text_from_input
from utils.generate_game import generate_game_structure
from utils.github_uploader import upload_game_to_github
from utils.feedback import log_feedback
from utils.llm_chat import llm_response
import os

# --- Inicialização do estado ---
if "jogo_gerado" not in st.session_state:
    st.session_state.jogo_gerado = None
if "fase_atual" not in st.session_state:
    st.session_state.fase_atual = 0
if "game_id" not in st.session_state:
    st.session_state.game_id = None

# --- Sidebar ---
with st.sidebar:
    st.image("assets/logo.png", use_column_width=True)
    
    st.markdown("### 💬 Fale com a IA")
    user_question = st.text_input("Pergunte algo sobre o artigo ou conteúdo.")
    if user_question:
        resposta = llm_response(user_question)
        st.markdown(f"**IA:** {resposta}")

    st.markdown("### 🛠️ Enviar feedback")
    feedback_text = st.text_area("Escreva um comentário ou sugestão.")
    if st.button("Enviar feedback"):
        log_feedback(feedback_text)
        st.success("Feedback enviado!")

# --- Corpo principal ---
st.title("🎮 Gerador de Jogos Educativos a partir de Artigos")

# Upload ou link
input_type = st.radio("Escolha a forma de envio:", ["Upload de arquivo", "Inserir link de artigo"])

uploaded_file = None
url = ""

if input_type == "Upload de arquivo":
    uploaded_file = st.file_uploader("Envie o artigo (.pdf ou .docx)", type=["pdf", "docx"])
else:
    url = st.text_input("Cole a URL do artigo")

if st.button("Gerar Jogo"):
    with st.spinner("Processando o artigo e gerando o jogo..."):
        texto = extract_text_from_input(uploaded_file, url)
        if not texto:
            st.error("Não foi possível extrair o texto do artigo.")
        else:
            game_id = f"jogo_{uuid.uuid4().hex[:8]}"
            jogo_gerado = generate_game_structure(texto)
            upload_game_to_github(uploaded_file, url, jogo_gerado, game_id)
            st.session_state.jogo_gerado = jogo_gerado
            st.session_state.fase_atual = 0
            st.session_state.game_id = game_id
            st.success("Jogo gerado com sucesso! A primeira fase será exibida abaixo.")

# --- Renderiza a fase atual, se já houver jogo gerado ---
if st.session_state.jogo_gerado:
    fase = st.session_state.jogo_gerado["fases"][st.session_state.fase_atual]
    st.header(f"Fase {st.session_state.fase_atual + 1}")
    st.markdown(f"**Conceito:** {fase['conceito']}")
    st.markdown(f"**Trecho do artigo:** {fase['trecho']}")
    st.markdown(f"**Explicação:** {fase['explicacao']}")
    st.markdown("**Mini-jogo:** (interação será implementada por tipo de fase)")

    if st.button("Avançar para próxima fase"):
        if st.session_state.fase_atual < 4:
            st.session_state.fase_atual += 1
        else:
            st.success("🎉 Fim do jogo!")
