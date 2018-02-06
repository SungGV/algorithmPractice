

def solution(n):
    lst =[-1 for _ in range(n+1)]
    lst[1] = 0


    for i in range(2, n+1):
        lst[i] = lst[i-1] + 1
        if i % 3 == 0 and lst[i] < lst[int(i/3)] + 1:
            lst[i] = lst[int(i/3)] + 1
        if i % 2 == 0 and lst[i] < lst[int(i/2)] + 1:
            lst[i] = lst[int(i/2)] + 1
    print('',list(range(11)))
    print(lst)

solution(10)
