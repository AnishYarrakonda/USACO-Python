n, q = list(map(int, input().split()))
grid = [input() for _ in range(n)]

def count_in_row(i):
    count = 0
    inside = False
    # 0 means "we are not currently in a +----+ sector"
    # 1 means "we have passed the first + in such a sector, and the other
    #   exit from it points up
    # -1 means it points down
    last_plus = 0
    for j in range(n):
        ch = grid[i][j]
        if ch == '|':
            inside = not inside
        elif ch == '.':
            if inside:
                count += 1
        elif ch == '+':
            if last_plus == 0:
                last_plus = 1 if grid[i-1][j] == '|' else -1
            else:
                curr_plus = 1 if grid[i-1][j] == '|' else -1
                if curr_plus != last_plus: # we actually crossed a border
                    inside = not inside
                last_plus = 0
    return count

counts_per_row = []
for i in range(n):
    counts_per_row.append(count_in_row(i))

curr_sum = sum(counts_per_row)
print(curr_sum)

for _ in range(q):
    ri = int(input().strip())-1
    rows = [input().strip() for _ in range(5)]
    for i in range(5):
        curr_sum -= counts_per_row[ri+i]
        grid[ri + i] = rows[i]
        counts_per_row[ri + i] = count_in_row(ri+i)
        curr_sum += counts_per_row[ri+i]
    print(curr_sum)