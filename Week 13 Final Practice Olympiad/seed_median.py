def multiplication_table_median(N):
    need = (N * N + 1) // 2

    lo, hi = 1, N * N
    while lo < hi:
        mid = (lo + hi) // 2

        count = 0
        for i in range(1, N + 1):
            count += min(N, mid // i)

        if count >= need:
            hi = mid
        else:
            lo = mid + 1

    return lo

N = int(input())
print(multiplication_table_median(N))