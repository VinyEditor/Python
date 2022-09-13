alt = float(input('Digite a sua altura em (m): '))
 
peso = float(input('Digite o seu peso (em Kg): '))
 
imc = peso / (alt * alt)
 
if imc < 25:
    print("Peso ideal")

else:
    print("Não está com peso ideal")
