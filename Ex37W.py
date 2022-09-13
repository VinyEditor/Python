print ("Tabuada do 1 ao 20")

tabuada = 1

while (tabuada <= 20):
    multiplicador = 0
    while (multiplicador < 11) :
        r = tabuada * multiplicador
        print (f"{tabuada} * {multiplicador} = {r}")
        multiplicador = multiplicador + 1
    tabuada = tabuada + 1
    input('Pressione uma tecla..')