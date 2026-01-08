N, Q = map(int, input().split())

XY = {(i, j): 0 for i in range(N) for j in range(N)}
YZ = XY.copy()
XZ = XY.copy()

total = 0
for _ in range(Q):
    x, y, z = map(int, input().split())
    xy, yz, xz = (x, y), (y, z), (x, z)
    XY[xy], YZ[yz], XZ[xz] = XY[xy] + 1, YZ[yz] + 1, XZ[xz] + 1
    total += (XY[xy] == N) + (YZ[yz] == N) + (XZ[xz] == N)
    print(total)