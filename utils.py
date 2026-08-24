import json
import os
from flask import render_template_string

def load_data(html):
    caminho = os.path.join(os.path.dirname(__file__), "static", "data", html)
    with open(caminho, 'r', encoding='utf-8') as file:
        dados_json = json.load(file)

    return dados_json

def load_template(html):
    lista = html.split('/')
    caminho = os.path.join(os.path.dirname(__file__), "static", "templates", *lista)
    with open(caminho, 'r') as file:
        dados = file.read()
    return dados

