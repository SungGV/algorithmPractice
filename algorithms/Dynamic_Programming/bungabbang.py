num = int(input())
price = str(input())
price = price.split()
price = list(map(lambda x: int(x), price))
price.insert(0,0)

def solution():
    cache = [0 for _ in range(num+1)]
    for i in range(1, num+1):
        for j in range(1, i+1):
            cache[i] = max(cache[i], cache[i-j] + price[j])
    return cache[num]

print(solution())

# comment