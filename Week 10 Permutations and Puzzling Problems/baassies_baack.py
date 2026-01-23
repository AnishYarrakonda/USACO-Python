def count_up_to(X):
    if X < 0:
        return 0

    sleep = {0, 1, 3, 6, 8}

    full_blocks = X // 9
    remainder = X % 9

    total = full_blocks * 5

    for r in range(remainder + 1):
        if r in sleep:
            total += 1

    return total

A, B = map(int, input().split())

print(count_up_to(B) - count_up_to(A - 1))