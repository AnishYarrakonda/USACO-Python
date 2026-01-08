N, M = map(int, input().split())
results = [""] + [" " + input() for i in range(N)]

def beats(a):
    beats_a = set()

    for i, result in enumerate(results[a]):
        if result == 'L':
            beats_a.add(i)

    for i in range(a+1, N+1):
        if results[i][a] == 'W':
            beats_a.add(i)

    return beats_a

def beats_both(a, b):
    return beats(a) & beats(b)

for _ in range(M):
    x, y = map(int, input().split())

    must_play = beats_both(x, y)
    l = len(must_play)
    pairs = l * (2 * N - l)

    print(pairs)