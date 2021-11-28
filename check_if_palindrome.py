def is_palindrome(word):
    a = word.lower()
    wordpalindrom = a == a[::-1]

    if wordpalindrom:
        return True
    else:
        return False