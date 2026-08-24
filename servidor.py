from flask import Flask, render_template_string, redirect, request
import views 

app = Flask(__name__)

app.static_folder = 'static'

@app.route('/')
def index():
    return render_template_string(views.index())

@app.route('/submit', methods=['POST'])
def submitar():
    titulo = request.form.get('titulo')
    detalhe = request.form.get('detalhes')
    views.submit(titulo, detalhe)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)