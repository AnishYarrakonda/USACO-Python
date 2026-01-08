N = int(input().strip())
sis = list(map(int, input().strip().split()))
fis = list(map(int, input().strip().split()))

events = []
for i in range(N):
    events.append((sis[i], 1))
    events.append((fis[i], -1))

events.sort(key=lambda x: (x[0], -x[1]))

current_cows = 0
max_cows = 0

for time, change in events:
    current_cows += change
    max_cows = max(max_cows, current_cows)

print(max_cows)
