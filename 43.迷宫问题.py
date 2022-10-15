n = int(input())
m = int(input())
maze = [[0 for i in range(m)]for j in range(n)]

for i in range(m):
    for j in range(n):
        maze[i][j] = int(input())


