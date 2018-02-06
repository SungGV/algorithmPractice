cache = [0,0,1]


given_num = 1000
i = 3
while len(cache) != given_num+1:
    cache.append(cache[i-1] + cache[i-2])
    i += 1
print(cache[-1] % 4294967291)
