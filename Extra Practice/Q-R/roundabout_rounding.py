# brute force solution
# pattern:
# 10^2 -> 5 = 5
# 10^3 -> 5 + 55 = 60
# 10^4 -> 5 + 55 + 555 = 615
# and so on

"""
def real_round(a, b):
    power = 10**b
    digit = a % power * 10 // power

    a = a // power * power

    if digit >= 5:
        a += power

    return a

def chain_round(a, b):
    for j in range(1, b+1):
        a = real_round(a, j)
    return a

T = int(input())

for _ in range(T):
    N = int(input())

    total = 0
    for i in range(2, N+1):
        digits = len(str(i))
        if real_round(i, digits) != chain_round(i, digits):
            total += 1

    print(total)
"""

import math

T = int(input())

for _ in range(T):
    N = int(input())

    if N < 45:
        print(0)
        continue

    fit_ten = int(math.log10(N-1))
    z = fit_ten - 1
    total = int((5 / 81) * (10 ** (z + 1) - 9 * z - 10))

    low = 5
    for i in range(1, fit_ten+1):
        low += 4 * 10 ** i

    high = 4 * 10**fit_ten
    for i in range(fit_ten):
        high += 9 * 10 ** i
    high = min(N, high)

    if high >= low:
        total += high - low + 1

    print(total)