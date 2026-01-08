N = int(input().strip())
pis = list(map(int, input().strip().split()))

average_flower_count = 0
for i in range(N):
    for j in range(i+1, N+1):
        photo = pis[i:j]
        average = sum(photo)/(j-i)
        if average in photo:
            average_flower_count += 1
print(average_flower_count)