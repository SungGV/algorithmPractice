import random

# rand_list = [random.randint(1,100) for i in range(10)]
rand_list = [7,4,3,5,6,7,8,10,6,43,654,4]


def binary_tree(data, begin, end, target):
    if begin > end:
        return -1 # not found
    mid = int((begin + end) / 2)
    if data[mid] == target:
        return target
    elif data[mid] < target:
        return binary_tree(data, mid+1, end, target)
    else:
        return binary_tree(data, begin, mid-1, target)

rand_list.sort()
print(rand_list)

print(binary_tree(rand_list, 0, len(rand_list), 5))