def rosnace():
    x = input('')
    moja_lista = x.split()

    z = len(moja_lista) - 1
    for i in range(0, z):
        if moja_lista[i] > moja_lista[i + 1]:
            print(moja_lista[i], moja_lista[i + 1])


rosnace()