from collections import Counter

N = int(input().strip())
xis = list(map(int, input().strip().split()))
sis = list(map(int, input().strip().split()))

# m and k are the speeds of the two horses
# b and c are their starting positions
# returns the x value or time at which they intersect
# if negative, then they never intersect
def intersection(m, b, k, c):
    # mx + b = kx + c
    # (m-k)x = c - b
    if m == k:
        return -1
    return (c-b)/(m-k)

important_times = set()

for i in range(N):
    for j in range(i+1, N):
        time = intersection(sis[i], xis[i], sis[j], xis[j])
        if time >= 0:
            important_times.add(time)

max_neck_and_neck = 1
for time in important_times:
    new_positions = [sis[i] * time + xis[i] for i in range(N)]
    counts = Counter(new_positions)
    max_neck_and_neck = max(max_neck_and_neck, counts.most_common(1)[0][1])

print(max_neck_and_neck)