'''
45656이란 수를 보자.

이 수는 인접한 모든 자리수의 차이가 1이 난다. 이런 수를 계단 수라고 한다.

세준이는 수의 길이가 N인 계단 수가 몇 개 있는지 궁금해졌다.

N이 주어질 때, 길이가 N인 계단 수가 총 몇 개 있는지 구하는 프로그램을 작성하시오. (0으로 시작하는 수는 없다.)

'''

n = 2

cache = [[1 for _ in range(10)] for _ in range(n+1)]
cache[1][0] = 0

for i in range(2, n+1):
    for j in range(10):
        cache[i][j] = 0

        if j > 0 :
            cache[i][j] += cache[i-1][j-1]
        if j < 9:
            cache[i][j] += cache[i - 1][j + 1]

print(sum(cache[-1]))