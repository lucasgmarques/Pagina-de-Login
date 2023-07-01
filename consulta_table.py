import mysql.connector

# Configurar as informações do banco de dados MySQL
db = mysql.connector.connect(
    host="localhost",
    user="lucas",
    password="123456789",
    database="auth"
)

# Consultar a tabela "usuarios"
cursor = db.cursor()
query = "SELECT * FROM usuarios"
cursor.execute(query)

# Obter os resultados da consulta
resultados = cursor.fetchall()

# Exibir os resultados
for resultado in resultados:
    print("ID:", resultado[0])
    print("Fullname:", resultado[1])
    print("Email:", resultado[2])
    print("Password:", resultado[3])
    print("---")

cursor.close()

