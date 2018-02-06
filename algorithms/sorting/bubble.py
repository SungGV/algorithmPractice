l = [99,88,66,55,44,33,22]

def bubble(l):

    for i in range(len(l)-1):
        for j in range(1, len(l)-i):
            if l[j-1] > l[j]:
                l[j], l[j-1] = l[j-1], l[j]
    return l

print(bubble(l))

