def flatten_array(array):
    result = list()

    for x in array:
        if isinstance(x, list):
            result.extend(flatten_array(x))
        else:
            result.append(x)
    return result