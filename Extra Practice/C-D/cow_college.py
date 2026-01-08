N = int(input())
C = sorted(list(map(int, input().split())))

max_profit = 0
best_cost = 100000000
for i in range(N):
    profit = (N-i) * C[i]
    if profit > max_profit:
        max_profit = profit
        best_cost = C[i]

print(max_profit, best_cost)