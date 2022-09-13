sex = input("Digite F para feminino ou M para masculino: ").upper()

while (sex != 'F' and sex != 'M'):
    print ('Opcão inválida, tente novamente!')
    sex = input("Digite F para feminino ou M para masculino: ").upper()

if (sex == 'F'):
    print ('Sexo Feminino!')
else: 
    print('Sexo Masculino!')