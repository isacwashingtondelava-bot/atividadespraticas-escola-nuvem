import requests

moeda = input("Digite a moeda (ex: USD, EUR): ").upper()
url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

try:
    response = requests.get(url)
    response.raise_for_status()

    dados = response.json()
    chave = f"{moeda}BRL"

    if chave not in dados:
        print("Moeda não encontrada.")
    else:
        info = dados[chave]
        print(f"Moeda: {moeda}/BRL")
        print(f"Valor atual: R$ {float(info['bid']):.2f}")
        print(f"Máxima: R$ {float(info['high']):.2f}")
        print(f"Mínima: R$ {float(info['low']):.2f}")
        print(f"Última atualização: {info['create_date']}")

except requests.exceptions.RequestException:
    print("Erro ao consultar a moeda.")