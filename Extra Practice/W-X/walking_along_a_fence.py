N, P = map(int, input().split())

posts = []
for _ in range(P):
    posts.append(tuple(map(int, input().split())))

point_to_dist = {}
dist = 0

for i in range(P):
    x1, y1 = posts[i]
    x2, y2 = posts[(i + 1) % P]

    dx = 0 if x1 == x2 else (1 if x2 > x1 else -1)
    dy = 0 if y1 == y2 else (1 if y2 > y1 else -1)

    x, y = x1, y1
    while (x, y) != (x2, y2):
        point_to_dist[(x, y)] = dist
        dist += 1
        x += dx
        y += dy

perimeter = len(point_to_dist)

for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    start, end = (x1, y1), (x2, y2)

    distance = abs(point_to_dist[start] - point_to_dist[end])
    true_distance = min(distance, perimeter-distance)

    print(true_distance)