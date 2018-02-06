'''
입력값은 한 행의 문자열로 주어지며, 각 값은 공백으로 구분된다.
첫 번째 값은 리스트를 회전하는 양과 방향(음수의 경우 좌측으로, 양수의 경우 우측으로 회전)이다.
첫 번째 값을 제외한 나머지 값은 리스트의 각 항목의 값이다.
회전된 리스트를 문자열로 출력한다.
구현에 이용할 자료구조에 대한 조건이나 제약은 없다.
입력되는 리스트의 항목의 개수는 유한한다.

입력: 1 10 20 30 40 50
출력: 50 10 20 30 40

'''

# inp = [1, 10, 20, 30, 40, 50]
inp = [4, '가', '나', '다', '라', '마', '바', '사']
# inp = [-2, 'A', 'B', 'C', 'D', 'E', 'F', 'G']
# inp = [0, 'A', 'B', 'C', 'D', 'E', 'F', 'G']

rotate_time = inp.pop(0)

if rotate_time < 0:
    rotate_time = len(inp) + rotate_time - 1


for _ in range(rotate_time):
    inp.insert(0, inp.pop())

print(inp)


#
# import collections
# datas = input("Input : ").split(" ")
# cycleList = collections.deque(datas[1:])
# cycleList.rotate(int(datas[0]))
# print("Output :", " ".join(cycleList))