
def adjacentNum(n):

    if n < 10:
        return n
    else:
        rst =''
        while len(str(n)) >= 2:
            rst += str(abs(int(str(n)[0]) - int(str(n)[1])))
            n = str(n)[1:]
        return adjacentNum(int(rst))


inp = str(input())
inp = inp.split()

a = int(inp[0])
b = int(inp[1])

cnt = 0
for i in range(a, b):
    rst = adjacentNum(i)
    if rst == 7 and rst >= a and rst <= b:
        cnt += 1
print(cnt)
