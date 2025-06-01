import json
import random
import requests
import streamlit as st
import re

def gerar_trechos(texto, n):
    paragrafos = [p.strip() for p in texto.split("\n") if len(p.strip()) > 50]
    if len(paragrafos) < n:
        paragrafos *= (n // len(paragrafos)) + 1
    return random.sample(paragrafos, n)

def validar_fase(fase):
    tipo = fase.get("tipo")
    conteudo = fase.get("conteudo")

    if tipo == "quiz_multipla_escolha":
        if not all(k in conteudo for k in ["pergunta", "alternativas", "correta"]):
            return False
        if len(conteudo["alternativas"]) != 4:
            return False

    elif tipo == "verdadeiro_ou_falso":
        if not all(k in conteudo for k in ["afirmacao", "correta"]):
            return False
        if conteudo["correta"] not in ["Verdadeiro", "Falso"]:
            return False

    elif tipo == "completar_texto":
        if not all(k in conteudo for k in ["texto_incompleto", "resposta"]):
            return False

    else:
        return False

    return True

def gerar_fase_llm(trecho):
    prompt = f"""
Você é um gerador de fases de jogo educativo em Streamlit.
A partir do seguinte trecho de artigo, gere uma fase que será representada por um JSON no formato abaixo:

Escolha o tipo de fase mais adequado entre:
- "quiz_multipla_escolha"
- "verdadeiro_ou_falso"
- "completar_texto"

Formato do JSON esperado:
{{
  "tipo": "quiz_multipla_escolha",
  "conteudo": {{
    "pergunta": "...",
    "alternativas": ["...", "...", "...", "..."],
    "correta": "..."
  }}
}}

Trecho:
{trecho.strip()}
"""

    hf_token = st.secrets["HF_TOKEN"]
    headers = {
        "Authorization": f"Bearer {hf_token}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "Qwen/Qwen2.5-7B-Instruct-Turbo",
        "messages": [
            {"role": "user", "content": prompt.strip()}
        ],
        "temperature": 0.7,
        "max_tokens": 600
    }

    try:
        response = requests.post(
            "https://router.huggingface.co/together/v1/chat/completions",
            headers=headers,
            json=payload,
            timeout=45
        )

        if response.status_code == 200:
            reply = response.json()["choices"][0]["message"]["content"]
            match = re.search(r'\{.*\}', reply, re.DOTALL)
            if match:
                return json.loads(match.group())
            else:
                print("⚠️ Resposta da LLM não contém JSON válido.")
        else:
            print(f"⚠️ Erro na resposta da LLM: status {response.status_code}")

    except Exception as e:
        print("Erro ao chamar a LLM:", e)

    return None

def generate_game_structure(texto):
    fases = []
    trechos = gerar_trechos(texto, 5)

    for trecho in trechos:
        fase = gerar_fase_llm(trecho)

        if fase and validar_fase(fase):
            fases.append(fase)
        else:
            print("Fase inválida, usando fallback.")
            fases.append({
                "tipo": "quiz_multipla_escolha",
                "conteudo": {
                    "pergunta": "Esse trecho não pôde ser convertido em uma fase válida.",
                    "alternativas": ["A", "B", "C", "D"],
                    "correta": "A"
                }
            })

    return fases
