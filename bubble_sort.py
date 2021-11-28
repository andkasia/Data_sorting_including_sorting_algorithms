def bubble_sort(moja_lista):
    for i in range(len(moja_lista)):
        for j in range(len(moja_lista) - 1):
            if moja_lista[j] > moja_lista[j + 1]:
                moja_lista[j], moja_lista[j + 1] = moja_lista[j + 1], moja_lista[j]


x = input('')
moja_lista = x.split()

bubble_sort(moja_lista)
print(*moja_lista)