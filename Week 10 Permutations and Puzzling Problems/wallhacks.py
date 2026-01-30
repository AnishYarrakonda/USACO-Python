n, k = map(int, input().split())

if k % 2 == 1:
    print(-1)
elif k < n-1:
    print(-1)
else:
    num_layers = (n - 1) // 2
    biggest_skip = 6 + 8 * (num_layers - 1)
    skip_needed = n**2 - 1 - k
    wallhacks = 0
    while skip_needed > 0:
        if skip_needed >= biggest_skip:
            wallhacks += 1
            skip_needed -= biggest_skip
        elif skip_needed >= biggest_skip - 6:
            wallhacks += 1
            skip_needed = 0
        biggest_skip -= 8
    print(wallhacks)