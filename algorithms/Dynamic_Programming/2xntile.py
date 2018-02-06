n = 5
cache = [0 for _ in range(n+1)]

cache[1] = 1
cache[2] = 2
for i in range(3, n+1):
    cache[i] = cache[i-1] + cache[i-2]


print(cache)