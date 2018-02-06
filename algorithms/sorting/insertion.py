l = [7,4,6,2,63,45,56,78,2,6,1]
l = [654,234,46,67,2,1,23,353,4654,74]
# def insertion(l):
#
#     for i in range(1, len(l)):
#         temp = l[i]
#         for j in range(i-1, -1, -1):
#             if temp < l[j]:
#                 l[j+1] = l[j]
#                 l[j] = temp
#             else:
#                 break
#     return l
# # print(insertion(l))
#
#
# def insertion2(l):
#     for i in range(1, len(l)):
#
#         temp = l[i]
#         j = i - 1
#         while j >= 0 and temp < l[j]:
#             l[j+1] = l[j]
#             j -= 1
#         l[j+1] = temp
#     return l
#
# print(insertion2(l))



def insertion(l):

    for i in range(1, len(l)):
        temp = l[i]
        j = i-1
        while j >= 0 and l[j] > temp:
            l[j+1] = l[j]
            l[j] = temp
            j -= 1

print(l)
insertion(l)
print(l)