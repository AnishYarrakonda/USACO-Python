N = int(input())
snakes = []
for _ in range(N):
    left, right = map(int, input().split())
    snakes.append([left, right])

snakes.sort(key=lambda x: x[1])

total = 0
i = 0
while i < len(snakes):
    point = snakes[i][1]
    total += 1
    while i < len(snakes) and snakes[i][0] <= point:
        i += 1

print(total)