import streamlit as st
import uuid
from utils.extract_text import extract_text_from_input
from utils.generate_game import generate_game_structure
from utils.github_uploader import upload_game_to_github
from utils.feedback import log_feedback
from utils.llm_chat import llm_sidebar_consultation
from phases.render_phase import render_fase

# --- Inicialização de estado ---
if "jogo_gerado" not in st.session_state:
    st.session_state.jogo_gerado = None
if "fase_atual" not in st.session_state:
    st.session_state.fase_atual = 0
if "game_id" not in st.session_state:
    st.session_state.game_id = None
if "pontuacao" not in st.session_state:
    st.session_state.pontuacao = 0

# --- Sidebar ---
with st.sidebar:
    llm_sidebar_consultation()

    st.markdown("📝 **Deixe um feedback**")
    feedback_text = st.text_area("Comentário ou sugestão:", key="feedback_area")
    if st.button("Enviar feedback", key="feedback_submit"):
        if feedback_text.strip():
            log_feedback(feedback_text)
            st.success("✅ Feedback enviado com sucesso!")
        else:
            st.warning("⚠️ Escreva algo antes de enviar.")

# --- Interface principal ---
st.title("🎮 Gerador de Jogos Educativos a partir de Artigos")

uploaded_file = st.file_uploader("Envie o artigo (.pdf ou .docx)", type=["pdf", "docx"])

if st.button("Gerar Jogo") and uploaded_file:
    with st.spinner("Processando o artigo e gerando o jogo..."):
        texto = extract_text_from_input(uploaded_file)

        if not texto or len(texto.split()) < 100:
            st.error("⚠️ O texto do artigo está muito curto ou não pôde ser extraído.")
            st.stop()

        game_id = f"jogo_{uuid.uuid4().hex[:8]}"
        fases = generate_game_structure(texto)
        jogo_gerado = {"fases": fases}  # ✅ encapsula corretamente

        upload_game_to_github(uploaded_file, None, jogo_gerado, game_id)

        st.session_state.jogo_gerado = jogo_gerado
        st.session_state.fase_atual = 0
        st.session_state.pontuacao = 0
        st.session_state.game_id = game_id

        st.success("✅ Jogo gerado com sucesso! Veja abaixo a primeira fase.")

# --- Execução do jogo ---
if st.session_state.jogo_gerado and st.session_state.fase_atual < 5:
    fase_idx = st.session_state.fase_atual
    fase = st.session_state.jogo_gerado["fases"][fase_idx]

    st.header(f"Fase {fase_idx + 1} de 5")
    st.markdown(f"**🔍 Conceito:** {fase['conceito']}")
    st.markdown(f"**📖 Trecho do artigo:**\n\n> {fase['trecho']}")
    st.markdown(f"**💡 Explicação:** {fase['explicacao']}")

    render_fase(fase)

    st.markdown("---")
    if st.button("➡️ Próxima fase"):
        st.session_state.fase_atual += 1

# --- Tela final ---
elif st.session_state.fase_atual == 5:
    st.success("🎉 Parabéns! Você completou todas as fases!")
    st.markdown(f"**Sua pontuação:** `{st.session_state.pontuacao}` de 5")

    if st.button("🔄 Voltar ao menu"):
        for key in ["jogo_gerado", "fase_atual", "pontuacao", "game_id"]:
            st.session_state.pop(key, None)
        st.rerun()
