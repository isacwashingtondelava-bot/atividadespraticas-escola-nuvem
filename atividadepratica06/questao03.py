import requests

cep = input("Digite o CEP (somente números): ")

url = f"https://viacep.com.br/ws/{cep}/json/"

try:
    response = requests.get(url)
    response.raise_for_status()

    dados = response.json()

    if "erro" in dados:
        print("CEP não encontrado.")
    else:
        print("Endereço encontrado:")
        print(f"Logradouro: {dados['logradouro']}")
        print(f"Bairro: {dados['bairro']}")
        print(f"Cidade: {dados['localidade']}")
        print(f"Estado: {dados['uf']}")

except requests.exceptions.RequestException:
    print("Erro ao consultar o CEP.")