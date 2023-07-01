from flask import Flask, render_template, request
from dotenv import load_dotenv
import mysql.connector
import os


# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Cria uma instância do app Flask
app = Flask(__name__)

# Configurar as informações do banco de dados MySQL
db_host= os.getenv('DB_HOST')
db_user= os.getenv('DB_USERNAME')
db_password= os.getenv('DB_PASSWORD')
db_database= os.getenv('DB_DATABASE')

# Conecta ao banco de dados
db = mysql.connector.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_database
)

# Função para validar o email
def validate_email(email):
    # Implemente suas próprias regras de validação de email aqui
    # Neste exemplo, verificamos apenas se o email contém um '@'
    if '@' not in email:
        return False
    return True

# Rota para a página de login
@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def process_login():
    email = request.form['email']
    password = request.form['password']

    cursor = db.cursor()
    query = "SELECT * FROM usuarios WHERE email = %s AND password = %s"
    values = (email, password)
    cursor.execute(query, values)

    user = cursor.fetchone()
    cursor.close()

    if user:
        # Usuário autenticado com sucesso
        return "Login bem-sucedido!"
    else:
        # Credenciais inválidas
        return "Credenciais inválidas. Tente novamente."

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

        # Validar o email
        if not validate_email(email):
            return "Por favor, forneça um email válido."

        cursor = db.cursor()
        query = "INSERT INTO usuarios (fullname, email, password) VALUES (%s, %s, %s)"
        values = (fullname, email, password)
        cursor.execute(query, values)
        db.commit()
        cursor.close()

        return "Usuário cadastrado com sucesso!"

    return render_template('cadastro.html')

if __name__ == '__main__':
    app.run()

