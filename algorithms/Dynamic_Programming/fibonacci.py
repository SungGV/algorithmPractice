# fibonacci bottom up

def fibonacci(n):
    lst = [i for i in range(n)]
    lst[0] = 1
    lst[1] = 1

    for i in range(2, n):
        lst[i] = lst[i-1] + lst[i-2]
    return lst[-1]

print(fibonacci(10))

# top up
lst = [0 for _ in range(11)]
def fibonacci2(n):

    if n <= 1:
        return n
    else:
        if lst[n] > 0:
            return lst[n]
        lst[n] = fibonacci2(n-1) + fibonacci2(n-2)
    return lst[n]

print(fibonacci2(10))
