import sys

n = int(input())
stones = [0] + list(map(int, input().split()))
n += 1
last_val = 0
prev_val_indices = {0: n-1}

for i in range(n-2, -1, -1):
    candidate = last_val + 1
    # We may not need to increase our candidate stamina.
    if ((last_val-1 in prev_val_indices) and
        stones[i] + last_val >= stones[prev_val_indices[last_val-1]]):
        candidate = last_val
    candidate = max(candidate, stones[i+1] - stones[i])
    prev_val_indices[candidate] = i
    last_val = candidate
    if i == 0:
        print(candidate)