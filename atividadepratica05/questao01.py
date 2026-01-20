def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta


# Exemplo de uso
valor = 150.00
porcentagem = 10

valor_gorjeta = calcular_gorjeta(valor, porcentagem)
print(f"Valor da gorjeta: R$ {valor_gorjeta:.2f}")