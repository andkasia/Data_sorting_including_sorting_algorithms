def is_pangram(word):
    a = word.lower()

    a = set(a)

    litera = [ch for ch in a if ord(ch) in range(ord('a'), ord('z') + 1)]

    if len(litera) == 26:
        return True
    else:
        return False