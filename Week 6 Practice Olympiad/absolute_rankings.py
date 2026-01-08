import math

n, k = map(int, input().split())
ais = list(map(int, input().split()))
ais.sort()

poss = []
# just find the right triangular number by brute force
tn_idx = 0
tn = 0
while k > tn:
    tn_idx += 1
    tn += tn_idx

candidates = []
for i in range(1, tn_idx + 1):
    for j in range(n - i):
        candidates.append(ais[j+i] - ais[j])

candidates.sort()
print(candidates[k-1])