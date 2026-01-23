N = int(input())

grid = [[0]*N for _ in range(N)]

x, y = 0, -1

cnt = 1

move = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

while cnt <= N*N:
    temp_x = x + dx[move%4]
    temp_y = y + dy[move%4]
    if 0 <= temp_x < N and 0 <= temp_y < N \
        and not grid[temp_x][temp_y]:
        x = temp_x
        y = temp_y
        grid[x][y] = cnt
        cnt += 1
    else:
        move += 1

for row in grid:
    print(*row)