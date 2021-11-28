def unique_dictionary(dictionary):
    temp = []
    slownik = dict()

    for key, value in dictionary.items():
        if value not in temp:
            temp.append(value)
            slownik[key] = value

    return slownik