from flask import Flask, render_template, request
import csv
import os

app = Flask(__name__)

csv_path = 'data/points.csv'
fieldnames = ['latitude', 'longitude']

def create_csv():
    if not os.path.isfile(csv_path):
        with open(csv_path, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_point', methods=['POST'])
def add_point():
    latitude = request.form['latitude']
    longitude = request.form['longitude']

    create_csv()

    with open(csv_path, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'latitude': latitude, 'longitude': longitude})

    return 'Ponto adicionado com sucesso!'
