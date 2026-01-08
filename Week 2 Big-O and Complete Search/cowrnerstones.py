R, C = map(int, input().strip().split())
grid = [list(map(int, input().strip().split())) for _ in range(R)]

# rotate matrix 90° since r^2 * c is more costly
# than r * c^2 since r is 6 times greater than c
# also swap R and C
# 36 times faster
grid = [list(reversed(col)) for col in zip(*grid)]
R, C = C, R

# rows are now referred to as columns and vice versa
real_max_sum = float('-inf')
for r1 in range(R-1):
    for r2 in range(r1+1, R):
        top1 = top2 = float('-inf')
        for c in range(C):
            c_sum = grid[r1][c] + grid[r2][c]
            if  c_sum > top1:
                top1, top2 = c_sum, top1
            elif c_sum > top2:
                top2 = c_sum
        real_max_sum = max(top1+top2, real_max_sum)
print(real_max_sum)