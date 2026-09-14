produtos = {
    "papel": {"preco": 10,"quantidade": 8},
    "caneta": {"preco": 10,"quantidade": 8},
    "pneu": {"preco": 10,"quantidade": 8}
}

valor_total = 0

for  nome,dados in produtos.items():
    total = dados["preco"] * dados["quantidade"]
    valor_total += dados["preco"] * dados["quantidade"]
    print(total)
print(valor_total)