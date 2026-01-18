B, R = map(int, input().split())
G = list(map(int, input().split()))
M = list(map(int, input().split()))

trueG = []
running = 0
for i in range(R):
    trueG.append(G[i] - running)
    running += M[i]

trueG.sort()

if R % 2 == 1:
    candidates = [trueG[R//2]]
else:
    candidates = [trueG[R//2-1], trueG[R//2]]

candidates = [max(1, min(B, c)) for c in candidates] + [1, B]

penalty = 1e18
for median in candidates:
    penalty = min(penalty, sum(abs(trueG[i] - median) for i in range(R)))

print(penalty)