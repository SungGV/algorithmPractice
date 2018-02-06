

def partition(l, start, end):

    pivot = l[end]
    i = start - 1

    for j in range(start, end):
        if l[j] < pivot:
            i += 1
            l[i], l[j] = l[j], l[i]

    l[i+1], l[end] = pivot, l[i+1]

    return i + 1


def quickSort(l, start, end):

    if end > start:
        p = partition(l, start, end)
        quickSort(l, start, p-1)
        quickSort(l, p+1, end)


l = [6,4,43,67,434,13,345,123,87,10,11,5,21,346,67]

print(l)
quickSort(l, 0, len(l)-1)
print(l)