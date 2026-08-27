from utils import load_template
from utils import pegar_dados

def index():
    template_inicial = ''
    dados = pegar_dados()
    lista_li = [load_template('componentes/note.html').format(id_editar=dic[0], valor=dic[0],
                                                              title=dic[1],
                                                              note=dic[2],
                                                              favorito= '⭐' if dic[3] == 1 else '') for dic in dados]
    for template in lista_li:
        template_inicial += template

    return load_template('index.html').format(notes=template_inicial)