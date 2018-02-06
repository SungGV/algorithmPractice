dim = str(input())
dim = dim.split()
r_row = int(dim[0])
c_col = int(dim[1])
mine = []
for i in range(r_row):
    mine.append(list(input()))


def add_count(i, j):   # out of index 가 안나도록 조건을 준 후 mine수 업데이트
    if i < 0 or i >= r_row: return
    if j < 0 or j >= c_col: return
    if mine[i][j] == '*': return

    if mine[i][j] == '.':
        mine[i][j] = 1
    else:
        mine[i][j] += 1

def get_around(row, col):      # 동서남북 인덱스 조합
    for i in range(row-1, row+2):
        for j in range(col-1, col+2):
            add_count(i, j)

def get_mine_num():
    for row in range(len(mine)):
        for col in range(len(mine[row])):
            if mine[row][col] == '*':
                get_around(row, col)
            elif mine[row][col] == '.':
                mine[row][col] = 0

get_mine_num()

for i in mine:
    for j in i:
        print(j, end='')
    print()