import math

MAX_H = 900

# Only compute these once. Unfortunately doing this even once is slow...
partners = {}
for c in range(5, int(1.42 * MAX_H)): # 1.42 is an upper bound on sqrt(2)
    c2 = c**2
    for a in range(3, c):
        a2 = a**2
        b2 = c2 - a2
        b = int(round(math.sqrt(b2), 0))
        if a < b and a2 + b**2 == c2:
            if a not in partners:
                partners[a] = {}
            partners[a][b] = c
            if b not in partners:
                partners[b] = {}
            partners[b][a] = c

def solve(w, h, partners):
    answer = [MAX_H]*12
    for a2 in range(3, h-2):
        if a2 not in partners:
            continue
        b1 = w - a2
        if b1 not in partners:
            continue
        for b2 in partners[b1]:
            c1 = h - b2
            if c1 not in partners:
                continue
            for c2 in partners[c1]:
                d1 = w - c2
                if d1 not in partners:
                    continue
                for d2 in partners[d1]:
                    a1 = h - d2
                    if a1 in partners[a2]:
                        a3 = partners[a1][a2]
                        b3 = partners[b1][b2]
                        c3 = partners[c1][c2]
                        d3 = partners[d1][d2]
                        s = set((a1, a2, a3, b1, b2, b3, c1, c2, c3, d1, d2, d3))
                        if len(s) < 12:
                            continue
                        candidate = list(s)
                        candidate.sort()
                        better = False
                        for i in range(12):
                            if candidate[i] < answer[i]:
                                better = True
                                break
                            elif candidate[i] > answer[i]:
                                better = False
                                break
                        if better:
                            answer = candidate
    return(answer)

t = int(input())
for _ in range(t):
    w, h = map(int, input().split())
    answer = solve(w, h, partners)
    if answer[0] == MAX_H:
        print("IMPOSSIBLE")
    else:
        print(" ".join([str(x) for x in answer]))