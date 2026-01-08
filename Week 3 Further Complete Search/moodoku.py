grid = [list(input().strip()) for _ in range(6)]

m_count_row = [0]*6
m_count_col = [0]*6
empty_cells = []

for i in range(6):
    for j in range(6):
        if grid[i][j] == 'M':
            m_count_row[i] += 1
            m_count_col[j] += 1
        elif grid[i][j] == '.':
            empty_cells.append((i, j))

if any(c > 2 for c in m_count_row) or any(c > 2 for c in m_count_col):
    print(0)
    exit()

ans = 0
total_empty = len(empty_cells)

def dfs(idx):
    global ans
    if idx == total_empty:
        if all(c == 2 for c in m_count_row) and all(c == 2 for c in m_count_col):
            ans += 1
        return

    r, c = empty_cells[idx]

    if m_count_row[r] < 2 and m_count_col[c] < 2:
        grid[r][c] = 'M'
        m_count_row[r] += 1
        m_count_col[c] += 1
        dfs(idx+1)
        m_count_row[r] -= 1
        m_count_col[c] -= 1
        grid[r][c] = '.'

    remaining_m_row = 2 - m_count_row[r]
    remaining_m_col = 2 - m_count_col[c]
    remaining_empty_row = sum(1 for j in range(6) if grid[r][j] == '.')
    remaining_empty_col = sum(1 for i in range(6) if grid[i][c] == '.')
    if remaining_m_row <= remaining_empty_row - 1 and remaining_m_col <= remaining_empty_col - 1:
        grid[r][c] = 'O'
        dfs(idx+1)
        grid[r][c] = '.'

dfs(0)
print(ans)