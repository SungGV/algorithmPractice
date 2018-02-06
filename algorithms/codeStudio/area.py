inp = [[1, 2, 4, 4],
        [2, 3, 5, 7],
        [3, 1, 6, 5],
        [7, 3, 8, 6]]


s = set()
for x1, y1, x2, y2 in inp:
    for x in range(x1, x2):
        for y in range(y1, y2):
            s.add((x,y))
print(sorted(s))
print(len(s))