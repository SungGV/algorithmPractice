'''
1-7
Write an algorithm such that if an element in an MxN matrix is 0, its entire row
and column are set to 0.

'''


'''
1-8
Assume you have a method isSubstring which checks if one word is a
substring of another. Given two strings, si and s2, write code to check if s2 is
a rotation of si using only one call to isSubstring (e.g.,"waterbottle"is a rotation
of "erbottlewat").
'''


def isSubstring(s1, s2):
    return s2 in s1

def isRotation(s1, s2):
    # check if length of s1 is equal to s2 and not empty
    if len(s1) == len(s2) and len(s1) >0:
#         'waterbottLewaterbottLe'
#            'erbottLewat'
        y = s1+s1
        return isSubstring(y, s2)
    return False
    

s1 = 'waterbottLe'
s2 = 'erbottLewat'

print(isRotation(s1, s2))