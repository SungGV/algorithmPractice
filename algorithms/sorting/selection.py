l = [543,32,56,7,2,34,7,8,4,234]
print(sorted(l))

def selection(l):
    for i in range(len(l)-1):
        max_ = l[0]
        max_idx = 0
        for j in range(1, len(l) - i):
            if max_ < l[j]:
                max_ = l[j]
                max_idx = j
        l[len(l)-1-i], l[max_idx] = max_, l[len(l)-1-i]
    return l

print(selection(l))
