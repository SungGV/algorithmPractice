s = 20000000
s = str(s)
s = s.split('.')
rst = ''

for ind, letter in enumerate(s[0][::-1]):
    rst = letter + rst
    if (ind+1) % 3 == 0:
        rst = ',' + rst

if len(s) > 1:
    rst+='.'+s[1]
print(rst)

