
import string


alt = float(input('Digite a sua altura em (m): '))
 
peso = float(input('Digite o seu peso (em Kg): '))

sexo = (input('Informe o sexo: '))
 
imc = peso / (alt * alt)
 
if imc < 19:
    print("Abaixo do peso!")
elif imc < 24:
    print("Peso ideal!")
else:
    print("Acima do peso!")