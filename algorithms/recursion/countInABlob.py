grid = [
        ['x', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
        [' ', 'x', 'x', ' ', ' ', 'x', ' ', ' '],
        ['x', 'x', ' ', ' ', 'x', ' ', 'x', ' '],
        [' ', ' ', ' ', ' ', ' ', 'x', ' ', ' '],
        [' ', 'x', ' ', 'x', ' ', 'x', ' ', ' '],
        [' ', 'x', ' ', 'x', ' ', 'x', ' ', ' '],
        ['x', ' ', ' ', ' ', 'x', ' ', ' ', 'x'],
        [' ', 'x', 'x', ' ', ' ', 'x', 'x', 'x'],
]

# checked position = 'r'
def blob(x, y):
    if x > len(grid[0]) - 1 or x < 0 or y > len(grid) - 1 or y < 0:
        return 0
    if grid[x][y] == ' ' or grid[x][y] == 'r':
        return 0
    else:
        grid[x][y] = 'r'
        return 1 +blob(x-1,y-1)+blob(x-1, y)+blob(x-1,y+1)+blob(x,y-1)+blob(x,y+1)+blob(x+1,y-1)+blob(x+1,y)+blob(x+1,y+1)



print(blob(0,0))

