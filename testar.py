# 4. Editar anotações 
# Permitir a edição de anotações existentes;

# Adicione um botão/link na nota para a função de editar. Ao
#  clicar no botão de edição, o usuário deve ser direcionado para uma página html nova de edição.
# Ao clicar no botão/link, o servidor deverá receber uma requisição no seguinte formato:

# GET /update/<NOTA_ID> HTTP/1.1
# Importante: O link ou botão deve possuir o atributo name='edit_button' para que o teste de editar anotações passe com sucesso.
# A página de edição deve apresentar um formulário com o título e conteúdo já preenchidos.
# Você precisará de um método novo no arquivo utils.py que recebe como argumento o id de uma anotação e retorna esta anotação no formato de um objeto do tipo Note.
# Esta página deve apresentar dois botões: Salvar e Cancelar. Caso os nomes sejam diferentes o teste de editar anotações não passará com sucesso.
# Ao clicar no botão/link de Cancelar o usuário deve ser direcionado para a página principal.
# Ao clicar no botão de Salvar a aplicação deve receber uma requisição no seguinte formato:

# POST /update HTTP/1.1
# <HTTP_HEADERS>

# id=<NOTA_ID>&titulo=<NOTA_TITULO>&detalhes=<NOTA_DETALHES>
# As alterações devem ser registradas no banco de dados e em seguida o usuário deve ser direcionado para a página inicial.