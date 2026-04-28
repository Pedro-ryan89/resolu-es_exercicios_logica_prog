name = input()
salario = float(input())
vendas = float(input())

comissao = vendas * 0.15
total = salario + comissao

print(f"TOTAL = R$ {total:.2f}")


