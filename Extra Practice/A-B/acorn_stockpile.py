N, X = map(int, input().split())
acorns = []

for _ in range(N):
    acorns.append(int(input()))

acorns.sort()

max_size = 0
left, right = 0, 1
while right < N:
    if acorns[right] - acorns[left] > X:
        max_size = max(right-left, max_size)
        left += 1
    else:
        right += 1
max_size = max(right-left, max_size)

print(max_size)