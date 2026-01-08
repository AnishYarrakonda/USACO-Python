Q = int(input().strip())
kernels = [1 for _ in range(100_000)]
kernels.insert(0, 0)
lit = 100_000

for _ in range(Q):
    switches = map(int, input().strip().split())
    for i in switches:
        lit += -1 if kernels[i] else 1
        kernels[i] = not kernels[i]
    print(lit)