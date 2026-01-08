N, B = map(int, input().split())

cows = []
X = {0}
Y = {0}

for _ in range(N):
    x, y = map(int, input().split())
    cows.append((x, y))
    X.add(x+1)
    Y.add(y+1)

def split(fence_x, fence_y):
    a = b = c = d = 0
    for xx, yy in cows:
        if xx > fence_x and yy > fence_y:
            a += 1
        elif xx <= fence_x and yy > fence_y:
            b += 1
        elif xx <= fence_x and yy <= fence_y:
            c += 1
        else:
            d += 1
    return max(a, b, c, d)

min_cows = 10**18
for x in X:
    for y in Y:
        min_cows = min(min_cows, split(x, y))

print(min_cows)