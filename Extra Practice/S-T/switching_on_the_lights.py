N, M = map(int, input().split())
on = [[False for _ in range(N)] for _ in range(N)]
seen = [[False for _ in range(N)] for _ in range(N)]
adj = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    a, b, x, y = map(int, input().split())
    adj[a-1][b-1].append((x-1, y-1))

on[0][0] = True

def switch_lights(p=0, q=0):
    seen[p][q] = True
    if not adj[p][q]:
        return

    for u, v in adj[p][q]:
        on[u][v] = True

    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for xx in range(N):
        for yy in range(N):
            if seen[xx][yy]:
                for dx, dy in moves:
                    u, v = xx + dx, yy + dy
                    if 0 <= u < N and 0 <= v < N and not seen[u][v] and on[u][v]:
                        switch_lights(u, v)
    return

switch_lights()

count = 0
for i in range(N):
    for j in range(N):
        count += on[i][j]

print(count)