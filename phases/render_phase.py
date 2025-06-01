import streamlit as st
from phases.quiz_multipla_escolha import render_quiz_multipla_escolha
from phases.verdadeiro_falso import render_verdadeiro_falso
from phases.completar_texto import render_completar_texto

# Dicionário para despacho dinâmico
tipo_para_render = {
    "quiz_multipla_escolha": render_quiz_multipla_escolha,
    "verdadeiro_falso": render_verdadeiro_falso,
    "completar_texto": render_completar_texto,
}

def render_fase(fase):
    tipo = fase.get("tipo")
    conteudo = fase.get("conteudo")
    if tipo in tipo_para_render:
        tipo_para_render[tipo](conteudo)
    else:
        st.warning("⚠️ Tipo de fase desconhecido ou mal formatado.")
