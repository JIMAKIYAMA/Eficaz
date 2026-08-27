from flask import Flask, render_template_string, redirect, request, render_template
import views
from utils import inserir, deletar, editar

app = Flask(__name__)

app.static_folder = 'static'

@app.route('/')
def index():
    return render_template_string(views.index())

@app.route('/submit', methods=['POST'])
def submitar():
    titulo = request.form.get('titulo')
    detalhe = request.form.get('detalhes')
    inserir((titulo, detalhe))
    return redirect('/')

@app.route('/delete', methods=['POST'])
def delete():
    id = request.form.get('id')
    if id:
        deletar(id)
    return redirect('/')

@app.route('/editar/<int:id>', methods=['POST','GET'])
def editar_(id):
    title = request.form.get('title')
    content = request.form.get('content')
    if title and content and id:
        editar(title, content, id)
        return redirect('/')
    return render_template('edicao.html',id_editar=id)

if __name__ == '__main__':
    app.run(debug=True)
