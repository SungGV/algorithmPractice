'''
Implement a method to perform basic string compression using the count of repeated characters
if compressed string is not less than original, then return the original
ex) aabbbbbcccaa
    a2b5c2a2
'''


def strCompressor(s1):
    cnt = 1
    pivot = ''
    rst = ''

    for i, letter in enumerate(s1[:-1]):
        if letter == s1[i + 1]:
            cnt += 1

        else:
            rst += str(letter + str(cnt))
            cnt = 1

        if i == len(s1[:-1]) - 1:
            if letter != s1[-1]:
                cnt = 1

    rst += str(s1[-1] + str(cnt))

    return rst


print(strCompressor('aabbbbbcccaa'))
print(strCompressor('aabbbbbcccab'))
print(strCompressor('kkkcccabcd'))
