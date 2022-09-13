from __future__ import division

N1 = int(input('Primeiro valor: '))

N2 = int(input('Segubndo valor: '))

opção = 0

while opção !=5:

    print('''[1] Multiplicao
      [2] Soma
      [3] Subtracao
      [4] Divisao
      [5] Fim do processo''')
opção = str(input('Qual é a sua opção? '))

    
if opção == 1:
        produto = N1 * N2
        print('O produto entre {N1} x {N2} é {produto} '.format(N1, N2, produto) )
elif opção == 2:
        soma = N1 + N2
        print('A soma entre {N1} + {N2} é {soma} '.format(N1, N2, soma) )
elif opção == 3:
        diferença = N1 - N2
        print('A diferença entre {N1} - {N2} é {diferença} '.format(N1, N2, diferença) )
elif opção == 4:
        divisão = N1 / N2
        print('A soma entre {N1} / {N2} é {divisão} '.format(N1, N2, divisão) )
        
        if N1 or N2 == 0 :
            print ('Não pode dividir por zero nem dividir zero')
elif opção == 5:
        print('Fim do processo')
else:
        print('Opção inválida. Tente novamente.')
print('Fim do Programa!')



