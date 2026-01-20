preco_original = float(input("Digite o preço do produto: R$ "))
percentual_desconto = float(input("Digite o desconto (%): "))

# Cálculo do desconto
valor_desconto = preco_original * (percentual_desconto / 100)

# Preço final
preco_final = preco_original - valor_desconto

# Exibição formatada
print(f"Preço original: R$ {preco_original:.2f}")
print(f"Desconto aplicado: {percentual_desconto}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Preço final: R$ {preco_final:.2f}")