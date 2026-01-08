with open("hps.in", "r") as f:
    N = int(f.readline())
    moves = [f.readline().strip() for _ in range(N)]

prefix_moves = []

h, p, s = 0, 0, 0
for move in moves:
    if move == "H":
        h += 1
    elif move == "P":
        p += 1
    else:
        s += 1
    prefix_moves.append((h, p, s))

max_wins = 0
h1, p1, s1 = prefix_moves[-1]
for i in range(N):
    h2, p2, s2 = prefix_moves[i]
    h3, p3, s3 = h1 - h2, p1 - p2, s1 - s2
    wins = max(h2, p2, s2) + max(h3, p3, s3)
    max_wins = max(max_wins, wins)

with open("hps.out", "w") as f:
    f.write(str(max_wins) + "\n")