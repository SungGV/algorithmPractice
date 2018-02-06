import string
import re

# create dictionary
letter = list(string.ascii_lowercase)
letter.remove('q')
letter.remove('z')
d = dict()
rst_d = dict()

cnt = 2
for i in range(len(letter)):
    d[letter[i]] = cnt
    if (i+1) % 3 == 0:
        cnt += 1

def store_in_dict(s):
    s = list(s)
    s.insert(3, '-')
    s = ''.join(s)
    rst_d[s] = rst_d.get(s, 0) + 1

def get_rid_of_hypen(s):
    s = ''.join(s.split('-')).lower()
    rst = ''
    for letter in s:
        rst += str(d.get(letter, letter))
    store_in_dict(rst)

get_rid_of_hypen('4873279')
get_rid_of_hypen('ITS-EASY')
get_rid_of_hypen('888-4567')
get_rid_of_hypen('3-10-10-10')
get_rid_of_hypen('888-GLOP')
get_rid_of_hypen('TUT-GLOP')
get_rid_of_hypen('967-11-11')
get_rid_of_hypen('310-GINO')
get_rid_of_hypen('F101010')
get_rid_of_hypen('888-1200')
get_rid_of_hypen('-4-8-7-3-2-7-9-')
get_rid_of_hypen('487-3279')


# printing
flag = False
for i in sorted(rst_d.keys()):
    if rst_d[i] > 1:
        print(i, rst_d[i])
        flag = True
if not flag:
    print('no dups')


