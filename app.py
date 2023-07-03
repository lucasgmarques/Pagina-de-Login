from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
import bcrypt
import mysql.connector

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Cria uma instância do aplicativo Flask
app = Flask(__name__)

# Configurações do banco de dados
db_host = os.getenv('DB_HOST')
db_username = os.getenv('DB_USERNAME')
db_password = os.getenv('DB_PASSWORD')
db_database = os.getenv('DB_DATABASE')

# Conecta ao banco de dados
db = mysql.connector.connect(
    host=db_host,
    user=db_username,
    password=db_password,
    database=db_database
)

# Rota inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota para a página de cadastro
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        fullname = request.form['fullname']
        email = request.form['email']
        password = request.form['password']

        # Verificar se todos os campos estão preenchidos
        if not fullname or not email or not password:
            return "Por favor, preencha todos os campos."

        # Validar o email (pode ser usado um método de validação personalizado)
        if not is_valid_email(email):
            return "Por favor, forneça um email válido."

        # Realizar o hashing seguro da senha
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        cursor = db.cursor()
        query = "INSERT INTO usuarios (fullname, email, password) VALUES (%s, %s, %s)"
        values = (fullname, email, hashed_password)
        cursor.execute(query, values)
        db.commit()
        cursor.close()

        return "Usuário cadastrado com sucesso!"

    return render_template('cadastro.html')

# Rota para a página de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        cursor = db.cursor(prepared=True)  # Cursor preparado para evitar ataques de injeção de SQL

        query = "SELECT password FROM usuarios WHERE email = %s"
        values = (email,)
        cursor.execute(query, values)

        result = cursor.fetchone()
        cursor.close()

        if result:
            hashed_password = result[0]

            if bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
                # Usuário autenticado com sucesso
                return "Login bem-sucedido!"
            else:
                # Credenciais inválidas
                return "Credenciais inválidas. Tente novamente."
        else:
            # Usuário não encontrado
            return "Usuário não encontrado."

    return render_template('login.html')

# Função para validar o email (pode ser substituída por uma validação personalizada)
def is_valid_email(email):
    # Implemente a lógica de validação do email aqui
    return "@" in email

# Executa o aplicativo Flask
if __name__ == '__main__':
    app.run()
