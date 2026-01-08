N, M = map(int, input().split())

regions = []
for _ in range(N):
  regions.append(list(map(int, input().split())))

ACs = []
for _ in range(M):
    ACs.append(tuple(map(int, input().split())))

min_cost = sum([ac[3] for ac in ACs])
for used in range(2**M):

    stalls = [0] * 101
    cost = 0
    for i in range(M):
        if used & (2**i):
            cost += ACs[i][3]
            for j in range(ACs[i][0], ACs[i][1] + 1):
                stalls[j] += ACs[i][2]

    valid = True
    for i in range(N):
        for stall in range(regions[i][0], regions[i][1]+1):
            valid = valid and stalls[stall] >= regions[i][2]

    if valid:
        min_cost = min(min_cost, cost)

print(min_cost)