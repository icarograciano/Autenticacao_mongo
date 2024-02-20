from flask import Flask, render_template, request, redirect, url_for, flash, session
from pymongo import MongoClient
from bson import ObjectId
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Chave secreta para proteger sessões
bcrypt = Bcrypt(app)  # Inicializa o Flask-Bcrypt

# Configurações do MongoDB
mongo_url = 'mongodb://localhost:27017/'
database_name = 'App_Gestao_Entrega'
collection_name = 'users'

# Conecta-se ao MongoDB e obtém a coleção de usuários
client = MongoClient(mongo_url)
db = client[database_name]
users_collection = db[collection_name]

# Rota principal, carrega a página de login
@app.route('/')
def index():
    return render_template('login.html')

# Rota de login
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Busca no banco de dados pelo usuário
    user_data = users_collection.find_one({'username': username})

    # Verifica se o usuário existe e a senha está correta
    if user_data and bcrypt.check_password_hash(user_data['password'], password):
        session['user_id'] = str(user_data['_id'])
        flash('success', 'Login feito com sucesso!')
        return redirect('welcome')
    else:
        flash('danger', 'Usuário ou senha inválidos!!')
        return redirect(url_for('index'))

# Rota de boas-vindas, acessível apenas para usuários autenticados
@app.route('/welcome')
def welcome():
    if 'user_id' in session:
        return render_template('welcome.html')
    else:
        flash('danger', 'Você precisa fazer login primeiro!')
        return redirect(url_for('index'))

# Rota de logout
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('success', 'Logout successful!')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
