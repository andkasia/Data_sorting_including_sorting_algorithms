def sort_przez_wybor(moja_lista):
    n = len(moja_lista)

    for i in range(n - 1):
        wartosc_min = i

        for j in range(i + 1, n):
            if moja_lista[j] < moja_lista[wartosc_min]:
                wartosc_min = j

        if wartosc_min != i:
            moja_lista_1 = moja_lista[i]
            moja_lista[i] = moja_lista[wartosc_min]
            moja_lista[wartosc_min] = moja_lista_1


x = input('')
moja_lista = x.split()

sort_przez_wybor(moja_lista)
print(*moja_lista)