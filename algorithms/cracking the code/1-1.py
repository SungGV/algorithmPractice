def isUniqueChar1(s):
    # using data structure: set
    str_set = set(s)
    if len(s) == len(str_set):  # check the length
        return True
    return False


def isUniqueChar2(s):
    # simple comparison of each character
    for i in range(len(s) - 1):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                return False
    return True


def isUniqueChar3(s):
    # using python function count
    for letter in s:
        if s.count(letter) > 1:
            return False
    return True


def isUniqueCharUsingASCII(s):
    # using ASCII
    if len(s) > 256:
        return False

    letter_bool = [False] * 256
    for letter in s:
        # ord returns ASCII
        if letter_bool[ord(letter)] is True:
            return False
        else:
            letter_bool[ord(letter)] = True
    return True


import unittest


class noDupTestClass(unittest.TestCase):

    test_data = [('a', True),
                 ('aa', False),
                 ('ab', True),
                 ('ab ', True),
                 ('', True),
                 (' ', True),
                 ('  ', False),
                 ('qwerty', True),
                 ('qwerte', False)
                 ]

    def runTest(self):
        for s, ans in self.test_data:
            r1 = isUniqueChar1(s)
            self.assertEqual(r1, ans)

            r2 = isUniqueChar2(s)
            self.assertEqual(r2, ans)

            r3 = isUniqueChar3(s)
            self.assertEqual(r3, ans)

            r4 = isUniqueCharUsingASCII(s)
            self.assertEqual(r4, ans)


if __name__ == "__main__":
    unittest.main()
