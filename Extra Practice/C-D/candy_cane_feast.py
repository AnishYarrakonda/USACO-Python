N, M = map(int, input().split())
cow = list(map(int, input().split()))
candy_canes = list(map(int, input().split()))

for candy_cane in candy_canes:
    if cow[0] >= candy_cane:
        cow[0] += candy_cane
    else:
        eaten = 0
        for i in range(N):
            if cow[i] > eaten:
                new_height = min(candy_cane, cow[i])
                cow[i] += new_height - eaten
                eaten = new_height

for c in cow:
    print(c)