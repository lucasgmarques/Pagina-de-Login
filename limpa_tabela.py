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

# Query para limpar a tabela "usuarios"
truncate_table_query = "TRUNCATE TABLE usuarios"

# Executa a query
cursor.execute(truncate_table_query)

# Confirma as alterações no banco de dados
conn.commit()

# Fecha a conexão com o banco de dados
conn.close()

