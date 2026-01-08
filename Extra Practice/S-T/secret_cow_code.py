import math

with open("cowcode.in", "r") as f:
    S, N = f.readline().split()
    N = int(N)

S = " " + S
L = len(S) - 1

def backtrack(x):
    if x <= L:
        return S[x]

    split = int(math.log2((x - 1) // L))
    block_len = L * (2 ** split)

    if x == block_len + 1:
        return backtrack(x - 1)
    else:
        return backtrack(x - block_len - 1)

result = backtrack(N)

with open("cowcode.out", "w") as f:
    f.write(result)