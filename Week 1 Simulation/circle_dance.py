p, r, k = map(int, input().split())
if k % 2 == 1:
    ccw_neigh = (((k - 2) + 2 * r) % p) + 1
    cw_neigh = ((k + 2 * r) % p) + 1
else:
    ccw_neigh = (((((k - 2) - 2 * r) % p) + p) % p) + 1
    cw_neigh = ((((k - 2 * r) % p) + p) % p) + 1
print(ccw_neigh, cw_neigh)