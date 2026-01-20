valor_reais = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15

# Conversões
valor_dolar = valor_reais / taxa_dolar
valor_euro = valor_reais / taxa_euro

# Exibição dos resultados
print(f"Valor em reais: R$ {valor_reais:.2f}")
print(f"Valor em dólares: US$ {valor_dolar:.2f}")
print(f"Valor em euros: € {valor_euro:.2f}")