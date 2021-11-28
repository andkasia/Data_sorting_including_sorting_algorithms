def merge_sorted_lists(list1, list2, n1, n2):
    list3 = [None] * (n1 + n2)
    i = 0
    j = 0
    k = 0

    while i < n1 and j < n2:

        if list1[i] < list2[j]:
            list3[k] = list1[i]
            k = k + 1
            i = i + 1
        else:
            list3[k] = list2[j]
            k = k + 1
            j = j + 1

    while i < n1:
        list3[k] = list1[i];
        k = k + 1
        i = i + 1

    while j < n2:
        list3[k] = list2[j];
        k = k + 1
        j = j + 1

    for i in range(n1 + n2):
        print(str(list3[i]), end=" ")


a = input("")
list1 = a.split()
n1 = len(list1)

b = input('')
list2 = b.split()
n2 = len(list2)

merge_sorted_lists(list1, list2, n1, n2)