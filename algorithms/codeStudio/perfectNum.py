def divisible(num):
    # skip its own number
    return [i  for i in range(1, num) if num % i == 0]


for i in range(1000):
    if sum(divisible(i)) == i:
        print(i)

