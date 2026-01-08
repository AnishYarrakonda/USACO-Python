T = int(input())

for _ in range(T):
    N = int(input())
    his = list(map(int, input().split()))

    f = 0
    for i in range(N):
        f += his[i] if i % 2 == 0 else -his[i]

    if N % 2 == 0:
        if f != 0:
            print(-1)
            continue
        f = 0
    else:
        if f < 0:
            print(-1)
            continue

    last_o = 0
    o = []
    valid = True

    for i in range(N - 1):
        o_i = his[i] - f - last_o
        if o_i < 0:
            valid = False
            break
        o.append(o_i)
        last_o = o_i

    if not valid:
        print(-1)
        continue

    if N % 2 == 0:
        mn = min(o[i] for i in range(0, N - 1, 2))
        for i in range(0, N - 1, 2):
            o[i] -= mn

    print(2 * sum(o))