with open("pails.in") as f:
    X, Y, M = map(int, f.read().split())

max_milk = 0
for i in range(M // X + 1):
    milk = X * i + Y * ((M - X * i) // Y)
    max_milk = max(max_milk, milk)

with open("pails.out", "w") as f:
    f.write(str(max_milk))