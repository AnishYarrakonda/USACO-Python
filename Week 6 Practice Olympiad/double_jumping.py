X, Y = map(int, input().split())
x_pos, y_pos = X > 0, Y > 0

abs_x, abs_y = abs(X), abs(Y)

if (abs_x + abs_y) % 2 == 0:
    print("IMPOSSIBLE")
else:
    result = []

    while (abs_x, abs_y) not in [(0, 0), (1, 0), (0, 1)]:
        if abs_x % 2 == 1:
            if ((abs_x - 1) // 2 + abs_y // 2) % 2 == 1:
                abs_x = (abs_x - 1) // 2
                abs_y = abs_y // 2
                result.append('R' if x_pos else 'L')
            else:
                abs_x = (abs_x + 1) // 2
                abs_y = abs_y // 2
                result.append('L' if x_pos else 'R')
        else:
            if (abs_x // 2 + (abs_y - 1) // 2) % 2 == 1:
                abs_x = abs_x // 2
                abs_y = (abs_y - 1) // 2
                result.append('U' if y_pos else 'D')
            else:
                abs_x = abs_x // 2
                abs_y = (abs_y + 1) // 2
                result.append('D' if y_pos else 'U')

    if abs_x == 1:
        result.append('R' if X > 0 else 'L')
    elif abs_y == 1:
        result.append('U' if Y > 0 else 'D')

    print("".join(result))