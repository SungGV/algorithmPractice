maze = [
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    [' ', 'x', 'x', ' ', 'x', 'x', ' ', 'x'],
    [' ', ' ', ' ', 'x', ' ', ' ', ' ', 'x'],
    [' ', 'x', ' ', ' ', 'x', 'x', ' ', ' '],
    [' ', 'x', 'x', 'x', ' ', ' ', 'x', 'x'],
    [' ', 'x', ' ', ' ', ' ', 'x', ' ', 'x'],
    [' ', ' ', ' ', 'x', ' ', ' ', ' ', 'x'],
    [' ', 'x', 'x', 'x', ' ', 'x', ' ', ' '],
]



path = []

def findPath(x, y):
    if x == len(maze[0]) - 1 and y == len(maze) - 1:
        maze[x][y] = '1'
        return True
    if -1 < x < len(maze[0]) and -1 < y < len(maze) and maze[x][y] == ' ':
        maze[x][y] = '1'
        if findPath(x, y + 1) or findPath(x, y - 1) \
        or findPath(x - 1, y) or findPath(x+1, y):
            print(x,y)
            return True
        maze[x][y] = '2'
        return False
    return False

for i in maze:
    print(i)
print(findPath(0, 0))

for i in maze:
    print(i)



#
#
#
# def findPath(x, y):
#     if x > len(maze[0]) - 1 or x < 0 or y > len(maze) - 1 or y < 0:  # wall
#         return False
#
#     if x == len(maze[0]) - 1 and y == len(maze) - 1:
#         maze[x][y] = '1'
#         return True
#     if maze[x][y] != ' ':  # if visited, blocked path
#         return False
#     else:
#         maze[x][y] = '1'
#         if findPath(x, y + 1) or findPath(x, y - 1) or findPath(x - 1, y) or findPath(x + 1, y):
#             return True
#         maze[x][y] = '2'
#         return False
#
#     return False



