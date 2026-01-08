T = int(input())

for _ in range(T):
    N = int(input())
    H = sorted((list(map(int, input().split()))))

    side = set()
    for i in range(N-1):
        if H[i] == H[i+1] and H[i] != H[-1]:
            side.add(H[i])

    print(2*len(side)+1)