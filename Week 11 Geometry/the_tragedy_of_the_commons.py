N = int(input())
rectangles = [tuple(map(int, input().split())) for _ in range(N)]

e = max(r[0] for r in rectangles)
f = max(r[1] for r in rectangles)
g = min(r[2] for r in rectangles)
h = min(r[3] for r in rectangles)

if e >= g or f >= h:
    print(0)
else:
    print(e, f, g, h)