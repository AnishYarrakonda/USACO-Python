T = int(input())
for _ in range(T):
    N = int(input())
    H = list(map(int, input().split()))

    liked_hays = set()
    for i in range(N-1):
        if H[i] == H[i+1]:
            liked_hays.add(H[i])

    for i in range(N-2):
        if H[i] == H[i+2]:
            liked_hays.add(H[i])

    liked_hays = list(liked_hays)
    liked_hays.sort()

    if liked_hays:
        print(*liked_hays)
    else:
        print(-1)