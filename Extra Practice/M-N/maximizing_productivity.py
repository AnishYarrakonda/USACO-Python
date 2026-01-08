N, Q = map(int, input().split())
C = list(map(int, input().split()))
T = list(map(int, input().split()))
farms = [C[i] - T[i] for i in range(N)]
farms.sort(reverse=True)

for _ in range(Q):
    V, S = map(int, input().split())
    print("YES" if farms[V-1] > S else "NO")