L1 = int(input('Digite o primeiro lado '))

L2 = int(input('Digite o segundo lado: '))

L3 = int(input('Digite o terceiro lado: '))

if L1  + L2 > L3 :
    print("É um triângulo")

else:
    print("Não é um triangulo")

if L1 == L2 or L3:   
    print("É um triângulo isósceles")

elif L1 == L2 == L3:
    print("É um triangulo equilátero")
else:
    print("É um triângulo escaleno")