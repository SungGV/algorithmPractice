'''
1.6 Given an image represented by an NxN matrix, where each pixel in the image is
4 bytes, write a method to rotate the image by 90 degrees. Can you do this in
place?
'''

x = [['p00', 'p01', 'p02', 'p03'],
     ['p10', 'p11', 'p12', 'p13'],
     ['p20', 'p21', 'p22', 'p23'],
     ['p30', 'p31', 'p32', 'p33']]


# the best version
def rotate(matrix):
    n = len(matrix)
    for layer in range(int(n / 2)):   # iterate 2
        first = layer   # 0
        last = n - 1 - layer   # 3
        for i in range(first, last):   # iterate 3 times
            offset = i - first   # i = 1, first = 0, offset = 1

            # save top
            top = matrix[first][i]

            # left -> top
            matrix[first][i] = matrix[last - offset][first]

            # bottom -> left
            matrix[last - offset][first] = matrix[last][last - offset]

            # right -> bottom
            matrix[last][last - offset] = matrix[i][last]

            # top -> right
            matrix[i][last] = top


rotate(x)

for i in x:
    print(i)


x = [['p00', 'p01', 'p02', 'p03'],
     ['p10', 'p11', 'p12', 'p13'],
     ['p20', 'p21', 'p22', 'p23'],
     ['p30', 'p31', 'p32', 'p33']]

# my way..


def rotate(matrix):
    l1 = []
    l2 = []
    for i in range(len(matrix)):  #
        for j in range(len(matrix[i]) - 1, -1, -1):
            l2.append(matrix[j][i])
        else:
            l1.append(l2)
            l2 = []
    return l1


x = [['p00', 'p01', 'p02', 'p03'],
     ['p10', 'p11', 'p12', 'p13'],
     ['p20', 'p21', 'p22', 'p23'],
     ['p30', 'p31', 'p32', 'p33']]


# pythonic way
# 90 degree
rotated90 = list(zip(*x[::-1]))
print(rotated90)

print()


def rotate_clockwise(matrix, degree=90):
    if degree not in [0, 90, 180, 270, 360]:
        pass
        # raise error or just return nothing or original
    return matrix if not degree else rotate_clockwise(list(zip(*matrix[::-1])), degree - 90)


print(rotate_clockwise(x, 180))

print()


def rotate_counterclockwise(matrix, degree=90):
    if degree not in [0, 90, 180, 270, 360]:
        pass
        # raise error or just return nothing or original
    return matrix if not degree else rotate_counterclockwise(list(zip(*matrix[::-1])), degree - 90)


print(rotate_counterclockwise(x, 90))
