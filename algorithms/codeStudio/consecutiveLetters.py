letter = 'aaabbcccccaaa'


prev = letter[0]
cnt = 1
rst = ''
for i in letter[1:]:
    if i == prev:
       cnt += 1
    else:
        rst += (prev + str(cnt))
        cnt = 1
    prev = i
rst += (prev + str(cnt))
print(rst)



s = 'aabcccaaaaas'

result = s[0]  # 첫번째 값을 결과에 넣는다
count  = 0   #

for st in s:
    if st == result[-1]:  #
        count += 1
    else:
        result += str(count) + st
        count = 1
result += str(count)

print (result)