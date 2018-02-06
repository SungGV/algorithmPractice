n = 2

cache = [[1 for i in range(10)] for _ in range(n+1)]

cache[1][0] = 0
for i in range(2, n + 1):
    for j in range(10):
        cache[i][j] = 0
        if j > 0:
            cache[i][j] += cache[i-1][j-1]
        if j < 9:
            cache[i][j] += cache[i - 1][j + 1]
        cache[i][j] % 1000000000


print(sum(cache[-1]) % 1000000000)