T = int(input().strip())

for _ in range(T):
    N, D = map(int, input().strip().split())
    ans = sorted(map(int, input().strip().split()))

    left, right = 0, 1
    found = False

    while right < N:
        diff = ans[right] - ans[left]
        if diff == D:
            found = True
            break
        elif diff < D:
            right += 1
        else:
            left += 1
            if left == right:
                right += 1

    print("YES" if found else "NO")