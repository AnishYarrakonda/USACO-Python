N = int(input())
F = sorted(list(map(int, input().split())), reverse=True)

total = F[0]
last = F[0]
for i in range(1, N):
    if last - F[i] >= 10:
        total += F[i]
        last = F[i]

print(total)