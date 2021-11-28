def get_largest_size(words):
    largest_word = ''
    for word in words:
        if len(word) > len(largest_word):
            largest_word = word
    return len(largest_word)