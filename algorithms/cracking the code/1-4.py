'''
write a method to replace all spaces in string with %20
'''


def replace(s1):
    return '%20'.join(s1.strip().split())


def replace2(s1):
    return s1.strip().replace(' ', '%20')


print(replace('mr john smith  '))
print(replace2('mr john smith  '))
