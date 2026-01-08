def ceilingDiv(a, b):
    return (a + b - 1) // b

def solve():
    n = int(input())
    h = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    t = [int(x) for x in input().split()]
    ord = [i for i in range(n)]
    ord.sort(key=lambda x: t[x])
    ret = 0
    for ordi in range(n - 1):
        i = ord[ordi]
        j = ord[ordi + 1]
        if h[i] < h[j] and a[i] > a[j]:
            ret = max(ret, ceilingDiv(h[j] - h[i] + 1, a[i] - a[j]))
    for i in range(n):
        h[i] += a[i] * ret
    for ordi in range(n - 1):
        i = ord[ordi]
        j = ord[ordi + 1]
        if h[i] <= h[j]: return -1
    return ret


t = int(input())
for _ in range(t):
    print(solve())