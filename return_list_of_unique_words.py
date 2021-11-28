def unique_elements(elements):
    unique_list = []

    for x in elements:
        if x in unique_list:
            continue
        else:
            unique_list.append(x)
    return unique_list