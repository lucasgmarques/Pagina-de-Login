from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Configurar as informações do banco de dados MySQL
db = mysql.connector.connect(
    host="localhost",
    user="lucas",
    password="123456789",
    database="auth"
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

