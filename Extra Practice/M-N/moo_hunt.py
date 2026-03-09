N, K = map(int, input().split())

moves = {}

for _ in range(K):
    x, y, z = map(int, input().split())
    if (x-1, y-1, z-1) not in moves:
        moves[(x-1, y-1, z-1)] = 0
    moves[(x-1, y-1, z-1)] += 1

ways = {}
max_score = 0
for i in range(2**N):
    score = 0
    for key, val in moves.items():
        x, y, z = key
        if i >> x & 1 and not i >> y & 1 and not i >> z & 1:
            score += val

    if score not in ways:
        ways[score] = 0
    ways[score] += 1

max_score = max(ways.keys())

print(max_score, ways[max_score])