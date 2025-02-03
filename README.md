# Flask GeoJSON Point Manager

Este é um projeto simples utilizando Flask para gerenciar pontos geográficos armazenados em um arquivo GeoJSON. O aplicativo permite adicionar, obter, atualizar e deletar pontos de um arquivo GeoJSON.

## Funcionalidades

- **Adicionar um ponto**: Envia as coordenadas (latitude e longitude), nome e observações para serem salvas em um arquivo GeoJSON.
- **Obter todos os pontos**: Retorna todos os pontos salvos no arquivo GeoJSON.
- **Atualizar um ponto**: Permite atualizar o nome e as observações de um ponto específico com base no ID.
- **Deletar um ponto**: Remove um ponto específico do arquivo GeoJSON com base no ID.

## Requisitos

- Python 3.x
- Flask

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/psiques/WebGis_Flask.git
   cd flask-geojson-point-manager
   
2. Instale as dependências:
   ```bash
   pip install -r flask

4. Execute o servidor Flask:
   ```bash
   python app.py
