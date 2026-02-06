import bisect

n, q = map(int, input().split())
his = list(map(int, input().split()))
his.sort()

for j in range(q):
    aj, bj = map(int, input().split())
    left = bisect.bisect_left(his, aj)
    right = bisect.bisect_right(his, bj)
    print(right-left)