row = 5
col = 5
board = [[-1 for i in range(col)] for j in range(row)]

x, y = 0, 0
cnt = 0
dx, dy = 0, 1
while board[x][y] == -1:
    board[x][y] = cnt
    cnt += 1
    x, y = x + dx, y + dy
    if x in [-1, row] or y in [-1, col] or board[x][y] != -1:
        x, y = x - dx, y - dy
        dx, dy = dy, -dx
        x, y = x + dx, y + dy

for i in board:
    print(' '.join(map(lambda x: str(x), i)))
