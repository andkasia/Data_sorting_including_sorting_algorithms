x = input('')
moja_lista = x.split()

if sorted(moja_lista) == moja_lista:
    print('Ciąg jest posortowany rosnąco')
else:
    print('Ciąg nie jest posortowany rosnąco')