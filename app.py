from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

# Caminho para o arquivo GeoJSON
geojson_path = 'data/points.geojson'

# Função para criar o arquivo GeoJSON se não existir
def create_geojson():
    if not os.path.isfile(geojson_path):
        os.makedirs('data', exist_ok=True) 
        with open(geojson_path, 'w') as f:
            json.dump({
                "type": "FeatureCollection",
                "features": []
            }, f)

# Rota principal para renderizar o template
@app.route('/')
def index():
    return render_template('index.html')

# Rota para adicionar um ponto
@app.route('/add_point', methods=['POST'])
def add_point():
    latitude = request.form['latitude']
    longitude = request.form['longitude']
    name = request.form.get('name', 'Sem Nome')  
    obs = request.form.get('obs', '') 

    create_geojson()

    # Ler o arquivo GeoJSON existente
    with open(geojson_path, 'r') as f:
        geojson_data = json.load(f)

    # Gerar um ID único
    new_id = len(geojson_data['features']) + 1

    # Adicionar o novo ponto
    new_feature = {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [float(longitude), float(latitude)]
        },
        "properties": {
            "id": new_id,  
            "name": name,
            "obs": obs
        }
    }
    geojson_data['features'].append(new_feature)

    # Salvar o arquivo GeoJSON atualizado
    with open(geojson_path, 'w') as f:
        json.dump(geojson_data, f)

    return jsonify(new_feature)  

# Rota para obter todos os pontos
@app.route('/get_points', methods=['GET'])
def get_points():
    if os.path.isfile(geojson_path):
        with open(geojson_path, 'r') as f:
            geojson_data = json.load(f)
        return jsonify(geojson_data)
    return jsonify({"type": "FeatureCollection", "features": []})

# Rota para atualizar um ponto
@app.route('/update_point', methods=['POST'])
def update_point():
    point_id = int(request.form['id'])
    name = request.form.get('name', '')
    obs = request.form.get('obs', '')

    if os.path.isfile(geojson_path):
        with open(geojson_path, 'r') as f:
            geojson_data = json.load(f)

        # Atualizar o ponto com o ID correspondente
        for feature in geojson_data['features']:
            if feature['properties']['id'] == point_id:
                feature['properties']['name'] = name
                feature['properties']['obs'] = obs
                break

        # Salvar o arquivo GeoJSON atualizado
        with open(geojson_path, 'w') as f:
            json.dump(geojson_data, f)

    return 'Ponto atualizado com sucesso!'

# Rota para deletar um ponto
@app.route('/delete_point', methods=['POST'])
def delete_point():
    point_id = int(request.form['id'])

    if os.path.isfile(geojson_path):
        with open(geojson_path, 'r') as f:
            geojson_data = json.load(f)

        # Filtrar os pontos para remover o ponto selecionado
        geojson_data['features'] = [
            feature for feature in geojson_data['features']
            if feature['properties']['id'] != point_id
        ]

        # Salvar o arquivo GeoJSON atualizado
        with open(geojson_path, 'w') as f:
            json.dump(geojson_data, f)

    return 'Ponto deletado com sucesso!'

if __name__ == '__main__':
    app.run(debug=True)
