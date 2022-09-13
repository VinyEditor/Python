v = int(input("Digite a quantidade de valores que você deseja: "))
s1 = 2
somador = 3
soma = 0

while (v < 0 or v > 50):
    print("Valor inválido!")
    v = int(input("Digite a quantidade de valores que você deseja: "))

print(s1)

while (v > 0):
    v = v - 1
    s2 = s1 + somador
    somador = somador + 2
    print(s2)
    s1 = s2
    soma = soma + s2 

#FIM