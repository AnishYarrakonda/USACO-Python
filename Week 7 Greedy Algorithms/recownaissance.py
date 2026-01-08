windows, cows, height = map(int, input().split())
W = sorted(list(map(int, input().split())))
C = sorted(list(map(int, input().split())))

total = 0
i = 0
j = 0

while i < windows and j < cows:
    if C[j] <= W[i]:
        j += 1
    elif C[j] >= W[i] + height:
        i += 1
    else:
        total += 1
        i += 1
        j += 1

print(total)