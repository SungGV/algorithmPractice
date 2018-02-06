def solution(x, y):
    prev = 0
    cnt = 0
    while x >=1 and y >= 1:
        if (x % 10) + (y % 10) + prev >= 10:
            prev = 1
            cnt += 1
        else:
            prev = 0
        x = x // 10
        y = y // 10
    print(cnt)

# input 받기
while True:
    inp = str(input())
    inp = inp.split()
    x = inp[0]
    y = inp[1]
    if int(x) != 0 and int(y) != 0:
        solution(int(x), int(y))
    else:
        break


