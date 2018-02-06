import random
import time
import itertools
t = time.time()
r = 100
c = 100

board = dict()
total = 0

direction = list(itertools.product((-1, 0, 1), repeat=2))
direction.remove((0, 0))

# random starting point
x = random.randint(0, r - 1)
y = random.randint(0, c - 1)
board[(x, y)] = 1
while len(board) < r*c:
    tempx, tempy = random.choice(direction)
    x += tempx
    y += tempy
    if x < 0:
        x = 0
    elif x > c-1:
        x = c-1
    if y < 0:
        y = 0
    elif y > r-1:
        y = r-1

    board[(x,y)] = board.get((x, y), 0) + 1
    total += 1

print(time.time() - t)
print(total)
print(board)