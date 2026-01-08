n, q = map(int, input().split())
S = input()

left = [[-1] * 26 for _ in range(n)]
right = [[n] * 26 for _ in range(n)]
right_exclude = [[n] * 26 for _ in range(n)]

for i, c in enumerate(S):
    left[i] = left[i - 1][:] if i else [-1] * 26
    left[i][ord(c) - ord('a')] = i

for i, c in reversed(list(enumerate(S))):
    right[i] = right[i + 1][:] if i + 1 < len(S) else [n] * 26
    right[i][ord(c) - ord('a')] = i

    best, sbest = n, n

    for j in range(26):
        if right[i][j] < best:
            sbest = best
            best = right[i][j]
        elif right[i][j] < sbest:
            sbest = right[i][j]

    for j in range(26):
        right_exclude[i][j] = sbest if right[i][j] == best else best

for _ in range(q):
    ql, qr = map(int, input().split())
    ql -= 1
    qr -= 1

    best = -1

    for t2 in range(26):
        k = left[qr][t2]
        i = right_exclude[ql][t2]

        if i >= k:
            continue

        for j in (left[(i + k) // 2][t2], right[(i + k) // 2][t2]):
            if j > i and j < k:
                best = max(best, (k - j) * (j - i))

    print(best)