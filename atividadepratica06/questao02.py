import requests

url = "https://randomuser.me/api/"

try:
    response = requests.get(url)
    response.raise_for_status()

    dados = response.json()
    usuario = dados["results"][0]

    nome = f"{usuario['name']['first']} {usuario['name']['last']}"
    email = usuario["email"]
    pais = usuario["location"]["country"]

    print("Usuário encontrado:")
    print(f"Nome: {nome}")
    print(f"E-mail: {email}")
    print(f"País: {pais}")

except requests.exceptions.RequestException:
    print("Falha ao conectar na API de usuários.")