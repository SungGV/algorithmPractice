'''
1.5 Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become
a2blc5a3. If the "compressed" string would not become smaller than the original
string, your method should return the original string.
'''

def stringCompressor(s1):
    
    pivot = s1[0]
    cnt = 1
    rst = ''
    for letter in s1[1:]:
        if pivot == letter:
            cnt += 1
        else:
            rst += str(pivot + str(cnt))
            cnt = 1
            pivot = letter
    return rst + pivot + str(cnt)

# print(stringCompressor('aaaabbccdeff'))
    
###### string buffer
# 
# 
# def stringCompressor2(s1):
#     if countCompression(s1) >= len(s1):
#         return s1
#     
#     
# def countCompression(s1):
#     if not(s1) or s1 == '': return 0
#     
#     pivot = s1[0]
#     cnt = 1
#     size = 0
#     for letter in s1[1:]:
#         if pivot == letter:
#             cnt += 1
#         else:
#             size += 1 + len(str(cnt))
#             cnt = 1
#             pivot = letter
#     return size + 1 + len(str(cnt))



# print(countCompression('aaaabbccdeff'))




'''
1.6 Given an image represented by an NxN matrix, where each pixel in the image is
4 bytes, write a method to rotate the image by 90 degrees. Can you do this in
place?
'''
# 
# 
# def showAsMatrix(mat):
#     [print(i) for i in mat]
#  
# def rotate(seq):
#     orig = list(seq)            # keep a copy of the original sequence
#     STEP = END = -1             # access elements N..0 one-by-one
#     r = range(len(seq[0])-1, END, STEP) # the length is fixed, calculate it only once
#     for idx, _ in enumerate(seq):
#         # list 0 consists of elements list[N][0], list[N-1][0], ..., list[0][0]
#         # list 1 consists of elements list[N][1], list[N-1][1], ..., list[0][1], etc.
#         seq[idx] = [orig[n][idx] for n in r]
#     return seq
#  
# def rotate2(seq):
#     import copy
#     size = len(seq)
#     matrix_new = copy.deepcopy(seq)
#     for i in xrange(size):
#         for j in reversed(range(size)):
#             matrix_new[i][size-1-j] = seq[j][i]
#     return matrix_new
#  
# def rotate3(seq):
#     return zip(*seq[::-1])
#  
# if __name__ == '__main__':
#     x = [ ['p00', 'p01', 'p02', 'p03'],
#           ['p10', 'p11', 'p12', 'p13'],
#           ['p20', 'p21', 'p22', 'p23'],
#           ['p30', 'p31', 'p32', 'p33'] ]
#  
#     print('original matrix')
#     showAsMatrix(x)
#     y = rotate(x)
#     print()
#     print('matrix rotated 90 degrees right')
#     showAsMatrix(y)
# 
# print()



def rotate(matrix):
    l1 = []
    l2 = []
    for i in range(len(matrix)):  # 
        for j in range(len(matrix[i])-1, -1, -1):
            l2.append(matrix[j][i])
        else: 
            l1.append(l2)
            l2 = []
    return l1





def roate2(matrix):
    n = len(matrix)
    for layer in range(int(n/2)):   # iterate 2
        first = layer   # 0
        last = n - 1 - layer   # 3
        for i in range(first, last):   # iterate 2 times
            offset = i - first  # i = 1, first = 0, offset = 1
            
            # save top
            top = matrix[first][i]
            
            # left -> top
            matrix[first][i] = matrix[last-offset][first]
            
            # bottom -> left
            matrix[last-offset][first] = matrix[last][last-offset]
            
            # right -> bottom
            matrix[last][last - offset] = matrix[i][last]
            
            # top -> right
            matrix[i][last] = top
    

x = [ ['p00', 'p01', 'p02', 'p03'],
      ['p10', 'p11', 'p12', 'p13'],
      ['p20', 'p21', 'p22', 'p23'],
      ['p30', 'p31', 'p32', 'p33'] ]

roate2(x)
for i in x:
    print(i)

def rotate3(matrix):
    
    n = len(matrix)
    
    for i in range(int(n/2)):
        col = i
        row = n - i - 1
        for j in range(col, row):
            
    
    

