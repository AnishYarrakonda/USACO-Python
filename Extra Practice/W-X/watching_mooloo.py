N, K = map(int, input().split())
D = list(map(int, input().split()))

total_cost = 0
i = 0

while i < N:
    start_day = D[i]
    end_day = D[i]

    while i + 1 < N and D[i + 1] - end_day <= K:
        i += 1
        end_day = D[i]

    cost = (end_day - start_day + 1) + K
    total_cost += cost

    i += 1

print(total_cost)