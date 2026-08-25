from utils import load_template, load_data
from flask import url_for
import os
import json

def index():
    template_inicial = ''
    lista_li = [load_template('componentes/note.html').format(title=dic.get('titulo'),
                                                            note=dic.get('detalhes')) for dic in load_data("notes.json")]
    
    for template in lista_li:
        template_inicial += template

    leitura_imagem = f"<img class='img' src = {url_for('static', filename='img/logo-getit.png')}>"
    return load_template('index.html').format(imagem=leitura_imagem, notes=template_inicial)

def submit(titulo, detalhe):
    caminho_json = os.path.join(os.path.dirname(__file__), 'static', 'data', 'notes.json')
    with open(caminho_json, 'r') as file:
        lista = json.load(file)
    lista.append({
        'titulo': titulo,
        'detalhes': detalhe
    })

    with open(caminho_json, 'w', encoding='utf-8') as file:
        json.dump(lista, file, indent=4)

    