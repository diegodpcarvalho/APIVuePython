from flask import Flask, request, jsonify
from flask_cors import CORS  # 📢 Certifique-se de importar!
import pandas as pd
import unicodedata

# Inicializar o app Flask
app = Flask(__name__)

# Configurar CORS corretamente
CORS(app, resources={r"/buscar": {"origins": "http://localhost:8080"}})

# Função para normalizar texto (remover acentos e tornar minúsculo)
def normalizar(texto):
    if isinstance(texto, str):
        return unicodedata.normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII').lower()
    return texto

# Carregar o CSV
try:
    df = pd.read_csv('Relatorio_cadop.csv', delimiter=';', encoding='utf-8')
    df = df.applymap(normalizar)  # Normalizar todas as células do DataFrame
except Exception as e:
    print(f"Erro ao carregar o arquivo CSV: {e}")

# Rota para busca
@app.route('/buscar', methods=['GET'])
def buscar():
    termo_busca = normalizar(request.args.get('q', ''))
    coluna_escolhida = request.args.get('coluna', '')

    colunas_relevantes = ['Registro_ANS', 'CNPJ', 'Nome_Fantasia', 'Cidade', 'UF', 'Representante']
    if coluna_escolhida not in colunas_relevantes:
        return jsonify({'error': 'Coluna inválida!'}), 400

    resultados = df[df[coluna_escolhida].astype(str).str.contains(termo_busca, na=False)]
    resultados = resultados[colunas_relevantes].fillna("")

    return jsonify(resultados.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
