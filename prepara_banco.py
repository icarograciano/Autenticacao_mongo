from flask_bcrypt import generate_password_hash
from pymongo import MongoClient

# Configurações do MongoDB
mongo_url = 'mongodb://localhost:27017/'
database_name = 'App_Gestao_Entrega'
collection_name = 'users'

# Dados do usuário para inserção
user_data = {
    'username': 'master',
    'email': 'master@master.com',
    'password': 'master123'  # A senha em texto plano
}

def prepare_database():
    # Conecta-se ao MongoDB
    client = MongoClient(mongo_url)
    db = client[database_name]

    # Cria a coleção se não existir
    if collection_name not in db.list_collection_names():
        db.create_collection(collection_name)

    # Gera o hash da senha usando Flask-Bcrypt
    hashed_password = generate_password_hash(user_data['password']).decode('utf-8')
    user_data['password'] = hashed_password

    # Insere o documento do usuário se não existir
    users_collection = db[collection_name]
    existing_user = users_collection.find_one({'username': user_data['username']})

    if not existing_user:
        users_collection.insert_one(user_data)
        print('Documento do usuário inserido com sucesso.')
    else:
        print('Documento do usuário já existe no banco.')

    # Fecha a conexão com o MongoDB
    client.close()

if __name__ == '__main__':
    prepare_database()
