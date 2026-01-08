N = int(input())
cows = []

for _ in range(N):
    pos, breed = input().split()
    cows.append((int(pos), breed))

cows.sort(key=lambda x: x[0])

max_size = 0
i = 0
while i < N:
    j = i
    while j < N and cows[j][1] == cows[i][1]:
        j += 1
    dist = cows[j-1][0] - cows[i][0]
    max_size = max(max_size, dist)
    i = j

prefix = []
running = 0
for i in range(N):
    running += 1 if cows[i][1] == "G" else -1
    prefix.append(running)

first_occurrence = {0: -1}

for i in range(N):
    if prefix[i] not in first_occurrence:
        first_occurrence[prefix[i]] = i

for idx in range(N):
    i = first_occurrence[prefix[idx]] + 1
    if idx == i-1:
        continue
    diff = cows[idx][0] - cows[i][0]
    max_size = max(diff, max_size)

print(max_size)