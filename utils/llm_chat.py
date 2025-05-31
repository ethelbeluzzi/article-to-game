import requests
import streamlit as st

def llm_response(prompt):
    api_url = "https://api-inference.huggingface.co/models/Qwen/Qwen1.5-1.8B-Chat"
    headers = {
        "Authorization": f"Bearer {st.secrets['HF_TOKEN']}",
        "Content-Type": "application/json"
    }

    body = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 150,
            "temperature": 0.7,
            "top_p": 0.95
        }
    }

    try:
        response = requests.post(api_url, headers=headers, json=body, timeout=20)
        response.raise_for_status()
        output = response.json()
        return output[0]["generated_text"] if isinstance(output, list) else output.get("generated_text", "⚠️ Erro no modelo.")
    except Exception as e:
        return f"⚠️ Erro ao consultar o modelo: {str(e)}"
