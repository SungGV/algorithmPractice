
def word_combine(s1):
    i = 0
    j = 1

    s1 = s1.strip().lower()
    word_list = []

    while j < len(s1):
        if s1[i].isalpha() and s1[j].isalpha():
            word_list.append(s1[i] + s1[j])
        i = j
        j += 1

    return word_list


def word_count(l1):
    l2 = dict()

    for i in l1:
        l2[i] = l2.get(i, 0) + 1
    return l2

def inter_uni(liter):
    intersec = 0
    union = 0
    for k in liter:
        i = l1.get(k, 0)
        j = l2.get(k, 0)
        if i != 0 and j != 0:  # intersection
            intersec += min(i, j)
            union += max(i, j)
        elif i == 0 and j != 0:
            union += j
        elif i != 0 and j == 0:
            union += i

    if intersec == 0 or union == 0:
        print(65536)
    else:
        print(intersec / union * 65536)


# s1 = 'FRANCE'
# s2 = 'french'

s1 = "E=M*C^2"
s2 = "e=m*c^2"

word_list1 = word_combine(s1)
word_list2 = word_combine(s2)


l1 = word_count(word_list1)
l2 = word_count(word_list2)
liter = set(list(l1.keys()) + list(l2.keys()))

inter_uni(liter)
