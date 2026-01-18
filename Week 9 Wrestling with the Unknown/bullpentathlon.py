import numpy as np

N = int(input())
bulls = [(i, list(map(int, input().split()))) for i in range(N)]
best = [[] for _ in range(5)]

for i in range(5):
    bulls.sort(reverse=True, key=lambda x : x[1][i])
    j = 0
    while j < N and j < 10:
        best[i].append(bulls[j])
        j += 1

max_score = 0
iterations = min(10, N)
for a in range(iterations):
    for b in range(iterations):
        for c in range(iterations):
            for d in range(iterations):
                for e in range(iterations):
                    nums = [a, b, c, d, e]
                    chosen = [best[i][nums[i]] for i in range(5)]

                    unique = set()
                    for thing in chosen:
                        unique.add(thing[0])
                    if len(unique) != 5:
                        continue

                    score = 0
                    for i in range(5):
                        score += chosen[i][1][i]
                    max_score = max(score, max_score)

print(max_score)