from flask import Flask, request
import mysql.connector

app = Flask(__name__)

# Connect to the MySQL database
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="yourdatabase"
)

# Create a cursor object to interact with the database
mycursor = mydb.cursor()

# Create a table to store user information
mycursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), password VARCHAR(255))")

# Endpoint to handle user registration
@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']

    # Insert user into the database
    sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
    val = (username, password)
    mycursor.execute(sql, val)
    mydb.commit()

    return "User registered successfully!"

if __name__ == '__main__':
    app.run()

