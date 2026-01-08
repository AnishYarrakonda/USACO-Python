N, T = map(int, input().split())
deliveries = [tuple(map(int, input().split())) for _ in range(N)]
deliveries.append((T, 0))
haybales, total, day = 0, 0, 1

for i in range(N):
    extra = 1 if i == N-1 else 0
    range_of_days = deliveries[i+1][0] - deliveries[i][0] + extra
    haybales += deliveries[i][1]
    eaten = min(haybales, range_of_days)
    total += eaten
    haybales -= eaten

print(total)