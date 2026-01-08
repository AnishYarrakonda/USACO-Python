n = int(input().strip())
ais = list(map(int, input().strip().split()))
ais_sorted = sorted(ais)

incorrect = 0
for i in range(n):
    if ais[i] != ais_sorted[i]:
        incorrect += 1
print(incorrect)