N, M, K = map(int, input().split())
theme_memory = {}

for night in range(N):
    good = True
    for theme in input().split():
        if (theme in theme_memory) and (night - theme_memory[theme] <= K):
            good = False
        theme_memory[theme] = night
    print("MOO" if good else "BOO")