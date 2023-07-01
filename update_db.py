import mysql.connector

# Configurar as informações do banco de dados MySQL
db = mysql.connector.connect(
    host="localhost",
    user="lucas",
    password="123456789",
    database="auth"
)

# Dados dos usuários a serem inseridos
usuarios = [
    {
        'fullname': 'João',
        'email': 'joao@example.com',
        'password': '123456789'
    },
    {
        'fullname': 'Maria',
        'email': 'maria@example.com',
        'password': '123456789'
    },
    {
        'fullname': 'Pedro',
        'email': 'pedro@example.com',
        'password': '123456789'
    }
]

# Inserir os usuários na tabela "usuarios"
cursor = db.cursor()
query = "INSERT INTO usuarios (fullname, email, password) VALUES (%s, %s, %s)"
for usuario in usuarios:
    values = (usuario['fullname'], usuario['email'], usuario['password'])
    cursor.execute(query, values)
db.commit()
cursor.close()

print("Usuários inseridos com sucesso!")
