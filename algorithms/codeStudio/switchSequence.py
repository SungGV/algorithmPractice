lst = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6']



while lst[-1] != lst[-1]:
    lst.insert(int(lst[-1][1:]), lst[-1])
    del lst[-1]

print(lst)