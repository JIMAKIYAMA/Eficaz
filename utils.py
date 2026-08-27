import os
import sqlite3
import json

def conectar():
    return sqlite3.connect('banco.db')

def inserir(dados):
    con = conectar()
    con.cursor().execute("INSERT INTO note (title, content) VALUES (?, ?)", dados)
    con.commit()
    con.close()

def pegar_dados():
    con = conectar()
    res = con.cursor().execute("SELECT * FROM note ORDER BY favoritado DESC").fetchall()
    con.close()
    return res

def pegar_nota(id):
    con = conectar()
    res = con.cursor().execute(
        "SELECT id, title, content FROM note WHERE id = ?", (id,)
    ).fetchone()
    con.close()
    res = ordenar()
    return res

def deletar(id):
    con = conectar()
    con.cursor().execute("DELETE FROM note WHERE id = ?", (id,))
    con.commit()
    con.close()

def editar(titulo, detalhe, id):
    con = conectar()
    con.cursor().execute(
        "UPDATE note SET title = ?, content = ? WHERE id = ?",
        (titulo, detalhe, id)
    )
    con.commit()
    con.close()

def trocar_favorito(id):
    con = conectar()
    
    con.cursor().execute(
            "UPDATE note SET favoritado = NOT favoritado WHERE id = ?",
            (id,)
        )
    con.commit()
    con.close()

def load_data(html):
    caminho = os.path.join(os.path.dirname(__file__), "static", "data", html)
    with open(caminho, 'r', encoding='utf-8') as file:
        dados_json = json.load(file)
    return dados_json

def load_template(html):
    lista = html.split('/')
    caminho = os.path.join(os.path.dirname(__file__), "templates", *lista)
    with open(caminho, 'r') as file:
        dados = file.read()
    return dados
