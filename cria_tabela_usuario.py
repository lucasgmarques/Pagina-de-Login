import mysql.connector

# Estabelece a conexão com o banco de dados
conn = mysql.connector.connect(
    host="localhost",
    user="lucas",
    password="123456789",
    database="auth"
)

# Cria o objeto cursor para executar as consultas SQL
cursor = conn.cursor()

# Exclui a tabela "usuarios" se ela existir
cursor.execute("DROP TABLE IF EXISTS usuarios")

# Cria a nova tabela "usuarios" com a estrutura fornecida
create_table_query = """
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fullname VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
)
"""
cursor.execute(create_table_query)

# Confirma as alterações no banco de dados
conn.commit()

# Fecha a conexão com o banco de dados
conn.close()

