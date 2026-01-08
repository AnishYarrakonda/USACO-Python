import bisect

N = int(input())
S = sorted(list(map(int, input().split())))

freq = {}
for s in S:
    if s not in freq:
        freq[s] = 0
    freq[s] += 1

ans = []

for i in range(3*N):
    s = S[i]
    if not freq[s]:
        continue

    freq[s] -= 1
    freq[2*s] -= 1
    freq[3*s] -= 1

    ans.append(s)

print(*ans, sep=" ")