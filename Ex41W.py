n = int (input('Digite um número inteiro menor que 100: '))

while (n > 99 or n < 0): 
    print("Número invalido! Tente novamente")
    n = int (input('Digite um número inteiro menor que 100: '))


s1 = 2 
somador = 3
soma = 0

print(s1)

while (n > 0):
    n = n - 1
    s2 = s1 + somador 
    somador = somador + 2
    print(s2) 
    s1=s2
    soma = soma + s2
print('Soma é igual: {}'.format(soma + 2))
    