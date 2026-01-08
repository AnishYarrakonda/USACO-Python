import heapq

with open("cowdance.in", "r") as f:
    N, T = map(int, f.readline().split())
    D = [int(f.readline()) for _ in range(N)]

def possible(k):
    cows = D[:k]
    heapq.heapify(cows)

    for i in range(k, N):
        earliest = heapq.heappop(cows)
        heapq.heappush(cows, earliest + D[i])

    return max(cows) <= T

left, right = 1, N

while left < right:
    mid = (left + right) // 2
    if possible(mid):
        right = mid
    else:
        left = mid + 1

with open("cowdance.out", "w") as f:
    f.write(str(left) + "\n")