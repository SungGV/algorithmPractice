n = int(input())
cache = [[0 for i in range(2)] for _ in range(n+1)]

cache[1][0] = 0
cache[1][1] = 1

for n in range(2, n+1):

    cache[n][0] = cache[n-1][0] + cache[n-1][1]
    cache[n][1] = cache[n - 1][0]

print(sum(cache[-1]))
