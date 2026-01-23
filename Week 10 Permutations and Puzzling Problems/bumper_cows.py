n, t = map(int, input().split())
dis = list(map(int, input().split()))
cis = list(map(int, input().split()))

answer = 0

for i in range(n):
    for j in range(i+1, n):
        smaller_c, larger_c = cis[i], cis[j]
        if smaller_c == larger_c:
            continue # they never collide
        # Find time of first collision
        smaller_d, larger_d = dis[i], dis[j]
        if smaller_d > larger_d:
            smaller_d, larger_d = larger_d, smaller_d
            smaller_c, larger_c = larger_c, smaller_c
        # Use 2 times the first collision time to avoid floating point
        if smaller_c == 1:
            twice_first_collision_time_ms = larger_d - smaller_d
        else:
            twice_first_collision_time_ms = smaller_d + (360 - larger_d)
        twice_t_ms = 2 * t
        if twice_t_ms >= twice_first_collision_time_ms:
            answer += 1
            twice_t_ms -= twice_first_collision_time_ms
        # After the first collision, every other collision takes 180 seconds.
        answer += twice_t_ms // 360
print(answer)