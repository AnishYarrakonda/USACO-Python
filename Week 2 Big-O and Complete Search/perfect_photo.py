M, N = map(int, input().strip().split())
gms = sorted(list(map(int, input().strip().split())))
hns = sorted(list(map(int, input().strip().split())))

min_dif = 10**18
i, j = 0, 0

while i < M and j < N:
    dif = abs(gms[i]-hns[j])
    min_dif = min(dif, min_dif)
    if gms[i] < hns[j]:
        i += 1
    else:
        j += 1

print(min_dif)