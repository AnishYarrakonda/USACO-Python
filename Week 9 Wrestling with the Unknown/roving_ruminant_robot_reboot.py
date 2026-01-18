T = int(input())

for _ in range(T):
    N, kD, kL, kR, kU = map(int, input().split())
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

    for i in range(16):
        print()