N, Q = map(int, input().strip().split())
differences = [0] * (N+2)

for _ in range(Q):
    S, A, B = map(int, input().strip().split())
    differences[A] += S
    differences[B+1] -= S

pots = []
running = 0
for i in range(1, N+1):
    running += differences[i]
    pots.append(running)

print(*pots)