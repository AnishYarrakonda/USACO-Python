N, B = map(int, input().strip().split())

def fib(prev, curr, n):
    if prev == curr == 0:
        return False
    while curr < n:
        prev, curr = curr, curr + prev
    if curr == n:
        return True
    return False

lowest_sum = 1001
for a0 in range(B+1):
    for a1 in range(B+1):
        if a0 + a1 > B:
            break
        if fib(a0, a1, N):
            lowest_sum = min(lowest_sum, a0+a1)

if lowest_sum == 1001:
    print(-1)
else:
    print(lowest_sum)