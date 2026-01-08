# My code is below
# It worked for smaller test cases but timed out due to large overlap between possible products

"""
from itertools import product

N = int(input())
S = input()

known_doubles = 0
for i in range(N-1):
    if S[i] == S[i+1] and S[i] != "F":
        known_doubles += 1

f_blocks = []
start = None
i = 0
while i < N:
    if S[i] == "F":
        start = max(i-1, 0)
        while i < N and S[i] == "F":
            i += 1
        f_blocks.append(S[start:i+1])
    i += 1

def get_possible(block):
    if block[0] == "F" or block[-1] == "F":
        possible = [k for k in range(len(block))]
    else:
        doubles = int((len(block) % 2 == 1) is not (block[0] == block[-1]))
        possible = []
        while doubles < len(block):
            possible.append(doubles)
            doubles += 2
    return possible

f_possible = []
for f_block in f_blocks:
    f_possible.append(get_possible(f_block))

excitement_levels = set()
for combination in product(*f_possible):
    excitement_levels.add(sum(combination) + known_doubles)

excitement_levels = sorted(list(excitement_levels))
print(len(excitement_levels))
print(*excitement_levels, sep="\n")
"""

# Solution code below
N = int(input())
S = input()

# Handle all-F case
if S.count('F') == N:
    S = 'E' + S[1:]

# Find all non-F positions
positions = [i for i in range(N) if S[i] != 'F']

# F's at the beginning and end can contribute 0 to this many doubles
ones = positions[0] + (N - 1 - positions[-1])

mn = 0
mx = 0

# For each consecutive pair of non-F characters
for i in range(len(positions) - 1):
    a = positions[i]
    b = positions[i + 1]
    gap = b - a
    different = (S[a] != S[b])

    # Minimum doubles in this gap
    mn += (gap & 1) ^ different

    # Maximum doubles in this gap
    mx += gap - different

# Generate all possible excitement levels
ans = []
step = 1 if ones > 0 else 2  # Step by 2 if no edge F's (parity constraint)
for i in range(mn, ones + mx + 1, step):
    ans.append(i)

print(len(ans))
print(*ans, sep='\n')