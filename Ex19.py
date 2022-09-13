P1 = float(input('Digite o valor da primeira nota: '))

P2 = float(input('Digite o valor da segunda prova:'))

MEDIA = (P1 + 2*P2) / 3

if MEDIA >= 5:
    print('Aprovado')
    
else:
    print('Reprovado')