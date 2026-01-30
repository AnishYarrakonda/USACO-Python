N, D = map(int, input().split())
times = []

for _ in range(N):
    F, S = map(int, input().split())
    times.append((D - F) / S)

T_max = max(times)
V_john = D / T_max

print(f"{V_john:.6f}")