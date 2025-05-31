from github import Github
import streamlit as st
import json
import datetime

def upload_game_to_github(uploaded_file, url, jogo_dict, game_id):
    token = st.secrets["GITHUB_TOKEN"]
    repo_name = st.secrets["REPO_NAME"]
    repo = Github(token).get_repo(repo_name)

    pasta_base = f"games/{game_id}/"
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 1. Salva o jogo_gerado.json
    jogo_json = json.dumps(jogo_dict, indent=2, ensure_ascii=False)
    jogo_path = pasta_base + "jogo_gerado.json"
    repo.create_file(jogo_path, f"Add jogo {game_id}", jogo_json, branch="main")

    # 2. Salva o artigo original
    if uploaded_file:
        conteudo = uploaded_file.read()
        nome = uploaded_file.name
        artigo_path = pasta_base + nome
        repo.create_file(artigo_path, f"Upload artigo original ({nome})", conteudo, branch="main")

    elif url:
        texto_url = f"Artigo extraído automaticamente de:\n{url}\n\nData: {timestamp}"
        artigo_path = pasta_base + "artigo_extraido.txt"
        repo.create_file(artigo_path, f"Upload artigo extraído de URL ({url})", texto_url, branch="main")
