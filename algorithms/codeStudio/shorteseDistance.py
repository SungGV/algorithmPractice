from collections import defaultdict
lst = [1,3, 7, 4, 8, 13, 17, 20]

d = defaultdict(list)
for i, j in list(zip(lst, lst[1:])):
    d[abs(i-j)].append((i,j))

print(d[min(d)])
