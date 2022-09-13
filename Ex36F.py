V = int(input(' Digite o valor: '))

while (V<0):
    print('O valor deve ser positivo')
    V = int(input(' Digite o valor: '))

ct  = int(input('Digite o começo da tabuada: '))
ft  = int(input('Digite o final da tabuada: '))

while (ct > ft):
    print('O segundo final deve ser maior.')
    ft = int(input('Digite o final da tabuada: '))

for i in range(ft,ct,-1):
    r = V * i
    print(f"{V} * {i} = {r} ")