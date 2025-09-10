import requests

try:
    resposta = requests.get("https://www.google.com")
    print(f"Status da requisição: {resposta.status_code}")
    print(f"Cabeçalhos da resposta: {resposta.headers}")
except requests.exceptions.RequestException as e:
    print(f"Ocorreu um erro na requisição: {e}")