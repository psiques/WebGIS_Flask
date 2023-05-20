from flask import Flask, render_template, request
import sqlite3
import os

def create_table():
    conn = sqlite3.connect('data/points.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS points
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 latitude REAL,
                 longitude REAL)''')
    conn.commit()
    conn.close()


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_point', methods=['POST'])
def add_point():
    latitude = request.form['latitude']
    longitude = request.form['longitude']

    db_path = 'data/points.db'
    if not os.path.isfile(db_path):
        # Cria uma conexão com o banco de dados
        conn = sqlite3.connect(db_path)
        
        # Executa uma operação qualquer para criar o arquivo
        # Por exemplo, podemos criar uma tabela vazia
        c = conn.cursor()
        c.execute("CREATE TABLE points (latitude REAL, longitude REAL)")
        
        # Salva as alterações e fecha a conexão
        conn.commit()
        conn.close()

    return 'Ponto adicionado com sucesso!'
