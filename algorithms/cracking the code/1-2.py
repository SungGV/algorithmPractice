# strin reverse


def stringReverse(s):
    s = list(s)
    for i in range(int(len(s) / 2)):
        s[i], s[len(s) - i - 1] = s[len(s) - i - 1], s[i]
    print(s)


def stringReverse2(s):
    print(s[::-1])


# using recursion
def stringReverse3(s):
    if s != '':
        return s[-1] + stringReverse3(s[:-1])
    else:
        return ""


print(stringReverse3('abcdefgh'))


# using stack and queue

def stringReverse4(s):
    l = list(s)  # stack
    rst = ''
    while len(l) >= 1:
        rst += l.pop()
    return rst


print(stringReverse4('abcdefgh'))
