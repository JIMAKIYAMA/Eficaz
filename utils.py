import json
import os
import sqlite3

def criar_banco_de_dados():
    con = sqlite3.connect('banco.db')
    cursor = con.cursor()
    cursor.execute("CREATE TABLE banco (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, content TEXT)")
    con.commit()
    return con

def inserir(dados):
    con = sqlite3.connect('banco.db')
    cursor = con.cursor()
    cursor.execute("""
    INSERT INTO banco (title, content) VALUES(?,?)
    """, dados)
    con.commit()

def pegar_dados():
    con = sqlite3.connect('banco.db')
    cursor = con.cursor()
    res = cursor.execute("SELECT id, title, content FROM banco")

    return res.fetchall()

def deletar(id):
    con = sqlite3.connect('banco.db')
    cursor = con.cursor()
    cursor.execute('DELETE FROM banco WHERE id = ?',(id,))
    con.commit()
    con.close()

def editar(titulo, detalhe, id):
    con = sqlite3.connect('banco.db')
    cursor = con.cursor()
    cursor.execute(
    """
    UPDATE banco SET title= ?, content = ? WHERE id = ?;
    """,
    (titulo, detalhe, id)
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
