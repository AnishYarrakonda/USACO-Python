import sys

NONE = -1
MULTIPLE = -2

r, c = map(int, input().split())

row_firsts = ['x' for _ in range(r)]
row_lasts = ['x' for _ in range(r)]
row_solos = [NONE for _ in range(r)]

col_firsts = ['x' for _ in range(c)]
col_lasts = ['x' for _ in range(c)]
col_solos = [NONE for _ in range(c)]

cols_needing_arrow = set()

for rr in range(r):
    s = input()
    for cc in range(c):
        symbol = s[cc]
        if symbol == '.':
            continue
        if row_solos[rr] == NONE:
            row_firsts[rr] = symbol
            row_solos[rr] = cc
        else:
            row_solos[rr] = MULTIPLE
        row_lasts[rr] = symbol
        if col_solos[cc] == NONE:
            col_firsts[cc] = symbol
            col_solos[cc] = rr
        else:
            col_solos[cc] = MULTIPLE
        col_lasts[cc] = symbol;
    if (row_solos[rr] != NONE) and (row_solos[rr] != MULTIPLE):
        cols_needing_arrow.add(row_solos[rr])

# Check for arrows that can't be pointed at other arrows.
for cc in cols_needing_arrow:
    if (col_solos[cc] != NONE) and (col_solos[cc] != MULTIPLE):
        print("IMPOSSIBLE")
        sys.exit(0)

answer = 0
for rr in range(r):
    if row_firsts[rr] == '<':
        answer += 1
    if row_lasts[rr] == '>':
        answer += 1
for cc in range(c):
    if col_firsts[cc] == '^':
        answer += 1
    if col_lasts[cc] == 'v':
        answer += 1

print(answer)