# read input
N = int(input())
line = list(input())
first = line[0]
line = list(map(lambda char: False if char == first else True, line))

# goal: make the binary representation equal to 0 by flipping

# flips every xth cow (x, 2x, 3x, ...)
def flip(x):
    for i in range(x-1, N, x):
        line[i] = not line[i]

cost = 0
for idx in range(1, N):
    if line[idx]:
        flip(idx+1)
        cost += idx + 1

print(cost)