
d_fn = lambda n: n + sum([int(i) for i in str(n)])


generator = set(d_fn(i) for i in range(1, 5000))
y = set(range(1,5000))

ans = y.difference(generator)

print(sum(ans))



def d_fn(n):
    y = n
    while n > 0:
        y += n % 10
        n //= 10
    return y

Z = [d_fn(n) for n in range(5000)]
A = [n for n in range(5000) if n not in Z]
print (sum(A))