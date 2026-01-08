def solve():
    N = int(input())
    H = list(map(int, input().split()))
    if H[-1] != 1:
        print(-1)
        return
    H = H[:-1]
    remaining = [False] + [True] * N
    for h in H:
        if not remaining[h]:
            print(-1)
            return
        remaining[h] = False
    ends = [x for x in range(1, N + 1) if remaining[x]]
    ans = [-1] * N
    l, r = 0, N - 1
    ans[l], ans[r] = ends
    for h in H:
        if ans[l] > ans[r]:
            l += 1
            ans[l] = h
        else:
            r -= 1
            ans[r] = h
    print(" ".join(map(str, ans)))


T = int(input())
for _ in range(T):
    solve()