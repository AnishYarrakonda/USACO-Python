N = int(input())
crops = []
freshness_sum = 0

for _ in range(N):
    t, f = map(int, input().split())
    crops.append((f, t))
    freshness_sum += f

crops.sort(key=lambda x: x[0] / x[1], reverse=True)

cost = 0
for f, t in crops:
    cost += t * freshness_sum
    freshness_sum -= f

print(cost)