N, M = map(int, input().split())
S = input()
A = list(map(int, input().split()))

def fuel1(i):
    total = 0

    j = (i-1) % N
    while S[j] == "R":
        total += A[j]
        j -= 1
        j %= N

    return total

def fuel2(i):
    total = 0

    j = (i + 2) % N
    while S[j] == "L":
        total += A[j]
        j += 1
        j %= N

    return total


milk = sum(A)

for idx in range(N):
    if S[idx] == "R" and S[(idx+1) % N] == "L":
        milk -= min(fuel1(idx), M)
        milk -= min(fuel2(idx), M)

print(milk)