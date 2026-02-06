K = int(input())

def valid(x):
    total = 0
    for i in range(1, 101):
        total += x // i
    return total >= K

lo, hi = 1, 10**16
while lo != hi:
    mid = (lo + hi) // 2

    if valid(mid):
        hi = mid
    else:
        lo = mid + 1

print(lo)