with open("cbarn.in") as f:
    N = int(f.readline())
    R = [int(f.readline()) for _ in range(N)]

min_dist = 10**18
for i in range(N):
    total_dist = 0
    for j in range(N):
        total_dist += R[(j + i) % N] * j
    min_dist = min(min_dist, total_dist)

with open("cbarn.out", "w") as f:
    f.write(str(min_dist))