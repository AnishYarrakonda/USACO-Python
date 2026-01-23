from collections import defaultdict

N = int(input())
grid = [input().strip() for _ in range(N)]

# Pad grid
grid = ["." * (N + 2)] + ["." + row + "." for row in grid] + ["." * (N + 2)]

INF = 10**9
best = [[INF] * (N + 2) for _ in range(N + 2)]

# Helper grid reused per direction
leg = [[0] * (N + 2) for _ in range(N + 2)]

# N
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if grid[i][j] == "*":
            leg[i][j] = leg[i - 1][j] + 1
            best[i][j] = min(best[i][j], leg[i][j])
        else:
            leg[i][j] = 0

# NE
for i in range(1, N + 1):
    for j in range(N, 0, -1):
        if grid[i][j] == "*":
            leg[i][j] = leg[i - 1][j + 1] + 1
            best[i][j] = min(best[i][j], leg[i][j])
        else:
            leg[i][j] = 0

# E
for i in range(1, N + 1):
    for j in range(N, 0, -1):
        if grid[i][j] == "*":
            leg[i][j] = leg[i][j + 1] + 1
            best[i][j] = min(best[i][j], leg[i][j])
        else:
            leg[i][j] = 0

# SE
for i in range(N, 0, -1):
    for j in range(N, 0, -1):
        if grid[i][j] == "*":
            leg[i][j] = leg[i + 1][j + 1] + 1
            best[i][j] = min(best[i][j], leg[i][j])
        else:
            leg[i][j] = 0

# S
for i in range(N, 0, -1):
    for j in range(1, N + 1):
        if grid[i][j] == "*":
            leg[i][j] = leg[i + 1][j] + 1
            best[i][j] = min(best[i][j], leg[i][j])
        else:
            leg[i][j] = 0

# SW
for i in range(N, 0, -1):
    for j in range(1, N + 1):
        if grid[i][j] == "*":
            leg[i][j] = leg[i + 1][j - 1] + 1
            best[i][j] = min(best[i][j], leg[i][j])
        else:
            leg[i][j] = 0

# W
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if grid[i][j] == "*":
            leg[i][j] = leg[i][j - 1] + 1
            best[i][j] = min(best[i][j], leg[i][j])
        else:
            leg[i][j] = 0

# NW
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if grid[i][j] == "*":
            leg[i][j] = leg[i - 1][j - 1] + 1
            best[i][j] = min(best[i][j], leg[i][j])
        else:
            leg[i][j] = 0

# Count spiders
count = defaultdict(int)
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if grid[i][j] == "*":
            count[best[i][j] - 1] += 1

max_k = max(count)
ans = [0] * (max_k + 1)

running = 0
for k in range(max_k, -1, -1):
    running += count[k]
    ans[k] = running

for x in ans:
    print(x)
