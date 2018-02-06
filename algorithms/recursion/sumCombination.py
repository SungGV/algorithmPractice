'''
n개의 계단이 있다.
어떤 사람이 계단을 오르려 하는데 이 사람은 계단을 한번에 1계단 2계단 또는 3계단씩 오를 수 있다.
이 사람이 계단을 오를수 있는 경우의 수를 1000으로 나눈 나머지를 구하여라

5=1+1+1+1+1
5=1+1+1+2
5=1+1+2+1
5=1+2+1+1
5=2+1+1+1
5=1+1+3
5=1+3+1
5=3+1+1
5=1+2+2
5=2+1+2
5=2+2+1
5=2+3
5=3+2
'''

def addition(n):

    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:

        return addition(n-3) + addition(n-2) + addition(n-1)

print(addition(7))


def bottom_up(n):
    lst = [-1 for _ in range(n+1)]

    lst[1] = 1
    lst[2] = 2
    lst[3] = 4

    for i in range(4, n+1):
        lst[i] = lst[i-1] + lst[i-2] + lst[i-3]
    return lst[n]

print(bottom_up(7))





