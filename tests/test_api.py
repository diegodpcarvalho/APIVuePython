import pytest
import requests

# URL da API Flask
BASE_URL = "http://127.0.0.1:5000"


# Teste 1: Verificar se a API está rodando
def test_api_online():
    response = requests.get(f"{BASE_URL}/buscar?q=santos&coluna=Cidade")
    assert response.status_code == 200  # API deve responder com sucesso


# Teste 2: Buscar um termo válido
def test_busca_valida():
    response = requests.get(f"{BASE_URL}/buscar?q=santos&coluna=Cidade")
    json_data = response.json()

    assert isinstance(json_data, list)  # Resposta deve ser uma lista
    assert len(json_data) > 0  # Deve haver pelo menos um resultado
    assert "Cidade" in json_data[0]  # Deve conter a chave "Cidade"


# Teste 3: Buscar uma coluna inválida
def test_coluna_invalida():
    response = requests.get(f"{BASE_URL}/buscar?q=santos&coluna=Inexistente")
    json_data = response.json()

    assert response.status_code == 400  # Deve retornar erro 400
    assert "error" in json_data  # Deve conter mensagem de erro


# Teste 4: Buscar sem parâmetro "q"
def test_busca_sem_parametro():
    response = requests.get(f"{BASE_URL}/buscar?coluna=Cidade")
    json_data = response.json()

    assert isinstance(json_data, list)  # Deve ser uma lista vazia ou com dados

