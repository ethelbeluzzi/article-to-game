from github import Github
import streamlit as st
import datetime
import html

def log_feedback(texto_feedback):
    if not texto_feedback.strip():
        return

    token = st.secrets["GITHUB_TOKEN"]
    repo_name = st.secrets["REPO_NAME"]
    feedback_path = st.secrets.get("FEEDBACK_FILE_PATH", "feedbacks/feedback.txt")

    gh = Github(token)
    repo = gh.get_repo(repo_name)

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    safe_text = html.escape(texto_feedback)
    full_entry = f"[{timestamp}] {safe_text}\n"

    try:
        file = repo.get_contents(feedback_path)
        conteudo_antigo = file.decoded_content.decode("utf-8")
        novo_conteudo = conteudo_antigo + full_entry
        repo.update_file(feedback_path, "Atualiza feedback", novo_conteudo, file.sha, branch="main")
    except Exception:
        # Se o arquivo não existir, cria
        repo.create_file(feedback_path, "Cria feedback.txt", full_entry, branch="main")
