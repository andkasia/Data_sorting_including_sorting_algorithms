def sort_przez_wstawianie(moja_lista):
    for i in range(1, len(moja_lista)):
        wartosc = moja_lista[i]
        pozycja = i

        while pozycja > 0 and moja_lista[pozycja - 1] < wartosc:
            moja_lista[pozycja] = moja_lista[pozycja - 1]
            pozycja = pozycja - 1

        moja_lista[pozycja] = wartosc


x = input('')
moja_lista = x.split()

sort_przez_wstawianie(moja_lista)
print(*moja_lista)