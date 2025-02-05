# Flask GeoJSON Geom Manager

Este aplicativo permite que os usuários interajam com o mapa, adicionem novos recursos (pontos, linhas, polígonos) e os gerenciem usando as tabelas de atributos. Aqui estão algumas coisas para abordar no código fornecido:
## Pontos-chave
- Modo de desenho: O modo de desenho alterna entre os modos de ponto, linha e polígono. Quando ativo, ele permite que os usuários desenhem essas geometrias no mapa. 
- Gerenciamento de tabela de atributos: Há três tabelas separadas para pontos, linhas e polígonos, e cada recurso pode ser editado ou excluído. Os dados são carregados dinamicamente de um servidor, e cada ação (como adicionar ou excluir recursos) aciona atualizações no mapa e nas tabelas. 
- Alternância do mapa base: Uma pequena miniatura permite que o usuário alterne entre duas camadas de base: OpenStreetMap e World Imagery da Esri.
 
![Capturar1](https://github.com/user-attachments/assets/8d6017be-74dd-4e37-9780-34edfe2c119d)
![Capturar2](https://github.com/user-attachments/assets/23282ad8-12fc-4e6a-99f0-6c9b3642ade0)

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

## Tecnologias
Leaflet.js | Flask (Python) | GeoJSON | HTML + CSS

## Acesse no navegador
   ```bash
👉 http://127.0.0.1:5000/


