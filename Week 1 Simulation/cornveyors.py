# > = Right = True
# < = Left = False

import copy

N, E = map(int, input().strip().split())
current_conveyors = [[char == ">" for char in input().strip()] for i in range(N)]
bins_per_cycle = [0] * 2**N
og_conveyors = copy.deepcopy(current_conveyors)

def sim_drop(conveyors, bins):
    idx = 0
    for row in conveyors:
        increment = 1 if row[idx] else 0
        row[idx] = not row[idx]
        idx = 2*idx + increment
    bins[idx] += 1

sim_drop(current_conveyors, bins_per_cycle)

period = 1
while current_conveyors != og_conveyors:
    sim_drop(current_conveyors, bins_per_cycle)
    period += 1

full_cycles, leftover_corns = divmod(E, period)
real_bins = list(map(lambda x: x*full_cycles, bins_per_cycle))

for _ in range(leftover_corns):
    sim_drop(current_conveyors, real_bins)

print(*real_bins)