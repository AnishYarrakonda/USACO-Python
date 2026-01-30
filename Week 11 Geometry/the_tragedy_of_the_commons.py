N = int(input())

rectangles = [tuple(map(int, input().split())) for _ in range(N)]


e = max(rectangles, key=lambda x : x[0])[0]
f = max(rectangles, key=lambda x : x[1])[1]
g = min(rectangles, key=lambda x : x[2])[2]
h = min(rectangles, key=lambda x : x[3])[3]


for a, b, c, d in rectangles:
    if not (c > e and g > a) and (d > f and h > b):
        print(0)
        exit()

print(e,f,g,h)