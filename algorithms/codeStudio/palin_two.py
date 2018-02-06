def bar(n):
    pLen = 1; lenTotal = 0; palindrome = None
    while lenTotal < n:
        palindromes = getPalindromes(pLen)
        lenTotal += len(palindromes)
        pLen += 1
    print(palindromes[n - (lenTotal+1)])

def getPalindromes(i):
    if i < 1: return []
    if i == 1: return [x for x in range(10)]
    lst = []
    half = i // 2
    if i % 2 == 0:
        for j in range(10 ** (half - 1), 10 ** half):
            lst.append(int(str(j)+str(j)[::-1]))
    else:
        for j in range(10 ** half, 10 ** (half + 1)):
            lst.append(int(str(j) + str(j)[:half][::-1]))
    lst.sort()
    return lst

# bar(1)
# bar(4)
bar(30)
# bar(100)
# bar(30000)
# bar(1000000)
