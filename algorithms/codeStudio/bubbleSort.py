import random
lst = [7,4,8,4,2,4,6,2,1,3,0]


for i in range(len(lst)-1):
    for j in range(len(lst)-1-i):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]

print(lst)


lst = [-3,6,-6,2,5,7,-1]
# 문제: 음수는 왼쪽 양수는 오른쪽으로
for i in range(len(lst)-1):
    for j in range(len(lst)-1-i):
        if lst[j] > 0 and lst[j+1] < 0:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]

print(lst)