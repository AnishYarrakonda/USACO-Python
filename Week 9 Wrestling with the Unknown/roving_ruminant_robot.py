N = int(input())
moves = input()

if N & 1:
    print(-1)
    exit()

x, y = 0, 0
for move in moves:
    match move:
        case "R":
            x += 1
        case "U":
            y += 1
        case "L":
            x -= 1
        case "D":
            y -= 1

print((abs(x)+abs(y))//2)