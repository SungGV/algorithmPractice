
def cola(n):
    if n <= 1:
        return
    else:
        if n % 2 == 0:
            n = (n/2)
        else:
            n = (3*n + 1)
        print(int(n))
        cola(n)




cola(5)
'''5
16
8
4
2
1
'''


