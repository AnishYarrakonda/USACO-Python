N = int(input())

cows = []
for _ in range(N):
    d, x, y = input().split()
    cows.append([d, int(x), int(y)])

stop_time = [float('inf')] * N

collisions = []
for i in range(N):
    for j in range(N):
        if i == j or cows[i][0] == cows[j][0]:
            continue

        if cows[i][0] == "N":
            north_idx, east_idx = i, j
        else:
            north_idx, east_idx = j, i

        n_x, n_y = cows[north_idx][1], cows[north_idx][2]
        e_x, e_y = cows[east_idx][1], cows[east_idx][2]

        if n_x > e_x and e_y > n_y:
            north_time = e_y - n_y
            east_time = n_x - e_x

            if north_time < east_time:
                collisions.append((east_time, east_idx, north_idx))
            elif east_time < north_time:
                collisions.append((north_time, north_idx, east_idx))

collisions.sort()

for time, blocked_cow, blocking_cow in collisions:
    if stop_time[blocking_cow] >= time:
        stop_time[blocked_cow] = min(stop_time[blocked_cow], time)

for i in range(N):
    if stop_time[i] == float('inf'):
        print("Infinity")
    else:
        print(stop_time[i])