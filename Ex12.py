Base = int(input('Digite o valor da base do triângulo: '))

Altura = int(input('Digite o valor da altura do triângulo: '))

Area = Base * Altura / 2

print("A área do triângulo acima é", Area)

if Area > 100:
    print("O terreno é grande")

else:  
    print("O terreno é pequeno")