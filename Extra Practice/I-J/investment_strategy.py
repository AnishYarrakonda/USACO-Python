N = int(input())
money = 1

for i in range(1, N+1):
    if i % 10 == 8:
        money //= 2

    if not i % 3:
        money += i

    if not i % 2:
        money = int(money * 1.1)

print(money)