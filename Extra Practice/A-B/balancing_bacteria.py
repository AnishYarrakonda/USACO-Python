# My code worked for smaller Ns but failed by timeout for larger Ns
#

"""

N = int(input())
patches = list(map(int, input().split()))

def spray(strength, s):
    j, dist = N-1, 0
    while dist < strength:
        patches[j] += (strength-dist) * s
        dist += 1
        j -= 1

total = 0
for i in range(1, N):
    if patches[i-1] == 0:
        continue

    sign = 1 if patches[i-1] > 0 else -1
    operations = abs(patches[i] - (patches[i-1] + sign))

    for _ in range(operations):
        spray(N-i, 1 if patches[i] < patches[i-1] + sign else -1)

    total += operations

print(total + 1)

"""

n = int(input())
a = list(map(int, input().split()))

ans = 0
contribution = 0
cnt_ops = 0

for i in range(n):
    contribution += cnt_ops
    a[i] += contribution

    cur_ops = -a[i]
    ans += abs(cur_ops)
    cnt_ops += cur_ops
    contribution += cur_ops

print(ans)