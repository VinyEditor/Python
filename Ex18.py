a = float(input('Digite o valor da aceleração: '))

v0 = float(input('Digite o valor da velocidade inicial: '))

t = float(input('Digite o valor do tempo do percurso: '))

V = v0 + (a. t) *3.6

if V<=40:
    print('Veículo muito lento')

elif V<=60:
    print('Velocidade permitida')

elif V<=80:
    print('Velocidade de cruzeiro')

elif V<=120:
    print('Veículo rápido')

else:
    print('Veículo muito rápido')
    
