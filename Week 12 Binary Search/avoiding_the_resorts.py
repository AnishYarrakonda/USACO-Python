import bisect

n = int(input())
lis = list(map(int, input().split()))
lis.sort()
q = int(input().strip())

for _ in range(q):
    xj, yj, zj = map(int, input().strip().split())
    curr_idx = xj - 1 # switch to 0-based indexing
    for __ in range(yj):
        # Be very careful when using any built-in binary search function!
        # Consult the documentation carefully -- remember that it's legal to
        #   do this during a contest. Make sure you don't end up using
        #   bisect_left where you want bisect_right, or vice versa.
        # Test on some small examples to make sure it's doing exactly what
        #   you want, even on edge cases.
        ins_point = bisect.bisect_left(lis, lis[curr_idx] + 1)
        lis[ins_point - 1] = lis[curr_idx] + 1
        curr_idx = ins_point - 1

    less_than_target = bisect.bisect_right(lis, zj - 1)
    print(n - less_than_target)