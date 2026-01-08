N = int(input())
line = list(map(int, list(input())))
infected_groups = []

start = None
i = 0
while i < N:
    if line[i]:
        start = i
        while i < N and line[i]:
            i += 1
        edge = start == 0 or i == N
        infected_groups.append((i - start, edge))
    else:
        i += 1

nights = 10**18
for group in infected_groups:
    if group[1]:
        nights = min(nights, group[0] - 1)
    else:
        nights = min(nights, (group[0] - 1) // 2)

infected = 0
squeeze = 2 * nights + 1
for group in infected_groups:
    infected += -(-group[0] // squeeze)

print(infected)