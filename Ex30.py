preco = float(input("Digite o preço do produto: "))

print("----- Condição de pagamento -----")
print("1 - À vista em dinheiro ou cheque, recebe 10% de desconto")
print("2 - À vista no cartão de crédito, recebe 15% de desconto")
print("3 - Em até 2x no cartão de crédito, preço normal")
print("4 - 3x ou mais no cartão de crédito, 20% de juros")
print("---------------------------------")

condicao = int(input("Digite a condição de pagamento: "))

if (condicao == 1):
    print(f"Valor final: R$ {preco - preco * 0.1}")
elif (condicao == 2):
    print(f"Valor final: R$ {preco - preco * 0.15}")
elif (condicao == 3):
    print(f"Valor da parcela: R$ {preco / 2}")
elif (condicao == 4):
    print(f"Valor da parcela: R$ {((preco * 0.2) + preco) / 3}")
else:
    print("Condição inválida")