from flask import Flask, request, jsonify
import sqlite3
from flask_cors import CORS # Importa o CORS

app = Flask(__name__)
CORS(app)
DB_NAME = 'desmatamento.db'

# ------------------- CRIAÇÃO DO BANCO E TABELAS -------------------
def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    # Amazônia
    c.execute('''CREATE TABLE IF NOT EXISTS amazonia (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    ano INTEGER UNIQUE,
                    area_desmatada REAL)''')

    # Cerrado
    c.execute('''CREATE TABLE IF NOT EXISTS cerrado (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    ano INTEGER UNIQUE,
                    area_desmatada REAL)''')

    # Queimadas
    c.execute('''CREATE TABLE IF NOT EXISTS queimadas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    ano INTEGER UNIQUE,
                    focos INTEGER)''')

    # Presidentes
    c.execute('''CREATE TABLE IF NOT EXISTS presidentes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT,
                    inicio INTEGER,
                    fim INTEGER,
                    taxa_media_anual REAL)''')

    conn.commit()
    conn.close()

# ------------------- INSERÇÃO INICIAL -------------------
def insert_initial_data():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    # Amazônia
    amazonia_data = [
        (1988, 21050), (1990, 13730), (1995, 29059), (2000, 18226), (2004, 27772),
        (2008, 12911), (2012, 4571), (2016, 7893), (2019, 10129), (2020, 10851),
        (2021, 13235), (2022, 11568), (2023, 9001)
    ]
    for ano, area in amazonia_data:
        c.execute("INSERT OR IGNORE INTO amazonia (ano, area_desmatada) VALUES (?, ?)", (ano, area))

    # Cerrado
    cerrado_data = [
        (2001, 13500), (2005, 11580), (2010, 7000), (2015, 9500), (2018, 6657),
        (2019, 6483), (2020, 7340), (2021, 8531), (2022, 10689), (2023, 9685)
    ]
    for ano, area in cerrado_data:
        c.execute("INSERT OR IGNORE INTO cerrado (ano, area_desmatada) VALUES (?, ?)", (ano, area))

    # Queimadas
    queimadas_data = [
        (2000, 115000), (2005, 226000), (2010, 85500), (2015, 183000), (2016, 184000),
        (2017, 205000), (2018, 194000), (2019, 197000), (2020, 222000), (2021, 184000),
        (2022, 172000), (2023, 156000)
    ]
    for ano, focos in queimadas_data:
        c.execute("INSERT OR IGNORE INTO queimadas (ano, focos) VALUES (?, ?)", (ano, focos))

    # Presidentes
    presidentes_data = [
        ("Sarney", 1985, 1990, 22400),
        ("Collor/Itamar", 1990, 1995, 17200),
        ("FHC", 1995, 2003, 19500),
        ("Lula", 2003, 2011, 15500),
        ("Dilma", 2011, 2016, 5420),
        ("Temer", 2016, 2019, 7536),
        ("Bolsonaro", 2019, 2022, 10500)
    ]
    for nome, inicio, fim, taxa in presidentes_data:
        c.execute("INSERT OR IGNORE INTO presidentes (nome, inicio, fim, taxa_media_anual) VALUES (?, ?, ?, ?)",
                  (nome, inicio, fim, taxa))

    conn.commit()
    conn.close()

# ------------------- ROTAS -------------------
@app.route('/amazonia', methods=['GET'])
def get_amazonia():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT ano, area_desmatada FROM amazonia ORDER BY ano")
    data = c.fetchall()
    conn.close()
    return jsonify(data)

@app.route('/cerrado', methods=['GET'])
def get_cerrado():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT ano, area_desmatada FROM cerrado ORDER BY ano")
    data = c.fetchall()
    conn.close()
    return jsonify(data)

@app.route('/queimadas', methods=['GET'])
def get_queimadas():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT ano, focos FROM queimadas ORDER BY ano")
    data = c.fetchall()
    conn.close()
    return jsonify(data)

@app.route('/presidentes', methods=['GET'])
def get_presidentes():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT nome, inicio, fim, taxa_media_anual FROM presidentes")
    data = c.fetchall()
    conn.close()
    return jsonify(data)

# ------------------- INICIALIZAÇÃO -------------------
if __name__ == '__main__':
    init_db()
    insert_initial_data()
    app.run(debug=True)
