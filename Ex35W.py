num = float(input('Digite o valor: '))
multiplicador = 1

while (num < 0):
    print('Não pode ser negativo')
    num = float(input('Digite o valor: '))

while (multiplicador > 0) and (multiplicador < 11):
   print(num * multiplicador)
   multiplicador = multiplicador + 1