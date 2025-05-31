import datetime
import html
import streamlit as st
from github import Github

def log_feedback(feedback_text):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Sanitiza o texto
    safe_text = html.escape(feedback_text)
    full_text = f"[{timestamp}] {safe_text}\n"

    token = st.secrets["GITHUB_TOKEN"]
    repo_name = st.secrets["REPO_NAME"]
    file_path = st.secrets.get("FEEDBACK_FILE_PATH", "feedbacks/feedback.txt")

    g = Github(token)
    repo = g.get_repo(repo_name)

    try:
        contents = repo.get_contents(file_path, ref="main")
        new_content = contents.decoded_content.decode() + full_text
        repo.update_file(file_path, "append feedback", new_content, contents.sha, branch="main")
    except Exception:
        repo.create_file(file_path, "create feedback log", full_text, branch="main")
