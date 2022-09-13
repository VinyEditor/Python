from os import ctermid
from signal import CTRL_BREAK_EVENT


V = int(input(' Digite o valor: '))

while (V<0):
    print('O valor deve ser positivo')
    V = int(input(' Digite o valor: '))

ct  = int(input('Digite o começo da tabuada: '))
ft  = int(input('Digite o final da tabuada: '))

while (ct > ft):
    print('O segundo final deve ser maior.')
    ft = int(input('Digite o final da tabuada: '))

while (ct < ft):
    print (V*ft)
    ft = ft - 1
    