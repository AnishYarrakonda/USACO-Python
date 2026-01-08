def purloined(N, xis):
    last = xis[0]-1
    for i in range(N):
        if xis[i] != last + 1:
            return last+1
        last = xis[i]
    return -1

real_N = int(input().strip())
real_xis = sorted(list(map(int, input().strip().split())))
print(purloined(real_N, real_xis))