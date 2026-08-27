from flask import Flask, render_template_string, redirect, request, render_template
import views
from utils import inserir, deletar, editar, pegar_nota, trocar_favorito

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

@app.route('/update/<int:id>', methods=['GET'])
def pagina_edicao(id):
    nota = pegar_nota(id)
    return render_template('edicao.html', nota=nota)

@app.route('/update', methods=['POST'])
def salvar_edicao():
    id = request.form.get('id')
    editar(request.form.get('titulo'), request.form.get('detalhes'), id)
    return redirect('/')

@app.route('/favoritar/<int:id>', methods=['POST'])
def favoritar(id):
    trocar_favorito(id)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
