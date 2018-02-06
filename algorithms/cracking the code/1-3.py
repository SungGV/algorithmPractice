# given two strings, write a method to decide if one is a permutation of the other


# by sorting
def isPermutation(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    if len(s1) != len(s2):
        return False
    return ''.join(sorted(s1)) == ''.join(sorted(s2))


def isPermutation2(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    for letter in s1:
        if s2.count(letter) == 0 or s1.count(letter) != s2.count(letter):
            return False
    return True


def isPermutation(s1, s2):
    if len(s1) != len(s2):
        return False
    s_bool = [0] * 256

    # count the number of each letter's occurance
    for letter in s1:
        s_bool[ord(letter)] += 1

    for letter in s2:
        s_bool[ord(letter)] = s_bool[ord(letter)] - 1
        if (s_bool[ord(letter)]) < 0:
            return False
    # check if the elements in list is all zero
    if sum(s_bool) != 0:
        return False

    return True


# print(isPermutation('abcd', 'acdbasda'))


def isPermutationUsingDic(s1, s2):
    d = {}
    for letter in s1:
        if letter not in d:
            d[letter] = 1
        else:
            d[letter] += 1

    for letter in s2:
        if letter not in d:
            return False
        else:
            d[letter] -= 1

    if sum(d.values()) != 0:
        return False

    return True


print(isPermutationUsingDic('abcdefffab', 'abcdffaeeb'))


# creating a list of permutations of a string

def createPermutation(s1):

    if len(s1) > 2:
        return [s1[0] + createPermutation(s1[1:])]
    else:
        return [s1[::-1]]


# print(createPermutation('abcd'))


def createPermutation(s1):
    if len(s1) == 0:
        return ['']
    prevList = createPermutation(s1[1:len(s1)])
    nextList = []
    for i in range(0, len(prevList)):
        for j in range(0, len(s1)):
            newString = prevList[i][0:j] + s1[0] + prevList[i][j:len(s1) - 1]
            if newString not in nextList:
                nextList.append(newString)
    return nextList


# print(createPermutation('abcd'))


def perms(s):
    if(len(s) == 1):
        return [s]
    result = []
    for i, v in enumerate(s):
        result += [v + p for p in perms(s[:i] + s[i + 1:])]
    return result


# print(perms('abcd'))


# try using dictionary and collection
# make a function that computes permutations of a string

# print(isPermutation2('ab c', 'bcA '))
