N = int(input())
pairs = [sorted(map(int, input().split())) for _ in range(N//2)]

total = 0
for i in range(len(pairs)):
    x1, y1 = pairs[i]

    for j in range(i+1, len(pairs)):
        x2, y2 = pairs[j]

        if (x1 < x2 < y1 < y2) or (x2 < x1 < y2 < y1):
            total += 1

print(total)