v = int(input("Digite a quantidade de valores que você deseja: "))

while (v < 0 or v > 20):
    print("Valor inválido!")
    n = int(input("Digite a quantidade de valores que você deseja: "))

nmenor = 1000000000000
soma = 0 
c = 0
nm = 0
pos = 0
neg = 0
porcen = 0

while (c < v):
    c = c + 1
    n = int(input("Digite um valor: "))
    if (nm < n):
        nm = n 
    elif (nmenor > n):
        nmenor = n
    soma = soma + n 
    media = soma / v 
    if (n < 0):
        neg = neg + 1
    else:
        pos = pos + 1
porcenNEG = (neg*100) / v
porcenPOS = (pos*100) / v
print("O maior valor digitado foi: {}".format(nm))
print("O menor valor digitado foi: {}".format(nmenor))
print("A soma de todos os valores é: {}".format(soma))
print("A média aritmética desses valores é: {:.2f}".format(media))
print("A porcentagem de valores positivos é: {}%".format(porcenPOS))
print("A porcentagem de valores negativos é: {}%".format(porcenNEG))