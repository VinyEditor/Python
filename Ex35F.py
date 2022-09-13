num = float(input('Digite o valor: '))

while (num < 0):
    print('Não pode ser negativo')
    num = float(input('Digite o valor: '))

while (num >= 0):
    for i in range(1,11,1):
        r = num * i
        print(num * i)
        break