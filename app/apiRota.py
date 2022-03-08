import flask
from flask.globals import request
from flask.templating import render_template
from user import User
import UsuarioDAO

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config['CORS_HEADERS'] = 'Content-Type'

 

@app.route('/cadastro', methods = ['GET'])
def cadastro():
	return render_template('cadastro.html')

@app.route('/cadastro', methods=['POST'])
def cadastro_post():	
	nome = request.form['name']
	sobreNome = request.form['lastname']
	email = request.form['email']
	senha = request.form['password']
	confSenha = request.form['confpassword']
	numbers = any(map(str.isdigit, senha))
	uppercases = any(map(str.isupper, senha))

	if (senha != confSenha):
		return render_template('cadastro.html')
	if (uppercases == False):
		return render_template('cadastro.html')
	if (numbers == False):
		return render_template('cadastro.html')

	usuario = User(None, nome, sobreNome, email, senha)
	UsuarioDAO.insertUser(usuario)
	return render_template('painel.html')


@app.route("/login", methods=['GET'])
def login():			
	return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
	email = request.form['email']
	senha = request.form['password']	
	listUsuario = UsuarioDAO.listAllUsers()

	for usuario in listUsuario:
		if email == usuario.getEmail():
			if senha == usuario.getSenha():
				return render_template('painel.html')
			else:
				return 	"<h1>Senha Não Confere!</h1>"

	
@app.route("/painel", methods=['GET'])
def painel():			
	return render_template('painel.html')
@app.route('/painel', methods=['GET'])
def painel_post():
	list = UsuarioDAO.listAllUsers()
	return (list)



@app.route('/delete', methods=['GET'])
def delete():
	return render_template('delete.html')

@app.route('/delete', methods=['POST'])
def delete_post():
	id = request.form['delete']
	intId = int(id)
	teste = User(intId,None,None,None,None)
	listUsuario = UsuarioDAO.listAllUsers()
	
	if id != True:
		UsuarioDAO.deleteUser(teste)
		return render_template('painel.html')
	else:
		return 	"<h1>Id Não Existe!</h1>"



@app.route('/update', methods=['GET'])
def update():
	return render_template('update.html')

@app.route('/update', methods=['POST'])
def update_post():
	id = request.form['id']
	idInt = int(id)
	nome = request.form['name']
	sobreNome = request.form['lastname']
	email = request.form['email']
	senha = request.form['password']
	confSenha = request.form['confpassword']

	if senha != confSenha:
		return "<h1>Senhas Não Confere!</h1>"

	usuario = User(idInt, nome, sobreNome, email, senha)
	UsuarioDAO.updateUser(usuario)
	return render_template('painel.html')


	
	



if __name__=="__main__":
	app.run()