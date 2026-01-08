T = int(input())    # number of subcases

for _ in range(T):
    # read in the input for each subcase
    input()
    N = int(input())
    desired = [list(input()) for _ in range(N)]
    K = int(input())
    stamp = [input() for _ in range(K)]
    painting = [['.' for _ in range(N)] for _ in range(N)]

    for rot in range(4):            # 4 rotations
        for i in range(N-K+1):      # N-K+1 rows
            for j in range(N-K+1):  # N-K+1 columns

                # make sure the stamp will only ink squares that need it
                if all(desired[i+a][j+b] == "*" or stamp[a][b] == "." for a in range(K) for b in range(K)):
                    # if it does, then actually ink the squares on the empty canvas
                    for a in range(K):
                        for b in range(K):
                            if stamp[a][b] == "*":
                                painting[i+a][j+b] = "*"

        stamp = [row[::-1] for row in zip(*stamp)]  # rotate the stamp 90 degrees CW

    print("YES" if painting == desired else "NO")   # print whether we could get the desired painting or not