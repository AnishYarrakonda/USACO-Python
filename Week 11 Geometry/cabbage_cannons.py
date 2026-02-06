b, e = map(int, input().split())
# Pad these just for convenience, so that the x=1 cannon is at index 1
#   rather than 0, etc.
sis = ["pad"] + list(map(int, input().split()))
tis = ["pad"] + list(map(int, input().split()))

# The idea of this solution is to take all the Essie cannons except the
#   one at y = 1, and shift them down to pretend they are at y = 1,
#   essentially exchanging distance for time.
# For example, a cannon at y = 3 that fires starting at T2 = 7 is kind of
#   equivalent to a cannon at y = 1 that fires starting at T2 = 5, in the
#   sense that both would collide with a cannon at x = 1 that fires starting
#   at T1 = 5.

# The keys of this dictionary are firing times of the shifted Essie cannons.
# The values are lists of *original* Essie y coordinates.
# We want these to be in reverse order of original y coordinate since if
#   there are multiple possible collisions for an x-cannon, the one with
#   the lower y coordinate will happen first.
# Hence, iterate through in reverse y order. This also saves us the need to
#   sort.
dc = {}
for y in range(e, 0, -1):
    # The equivalent T_j of the shifted cannon.
    shifted_to_y_1 = tis[y] - (y - 1)
    if shifted_to_y_1 not in dc:
        dc[shifted_to_y_1] = []
    dc[shifted_to_y_1].append(y)

# Hold the answer (which Essie cannons were responsible for collisions with
#   Bessie cannons)
b_annihilators = ["pad"] + [0] * b
for x in range(1, b+1):
    # The firing time a y-cannon at y = 1 would need to have to collide
    #   with this cannon.
    need = sis[x] - x + 1
    if need in dc and dc[need]:
        b_annihilators[x] = dc[need][-1]
        dc[need].pop() # remove the last element of the list

print(" ".join([str(x) for x in b_annihilators[1:]]))