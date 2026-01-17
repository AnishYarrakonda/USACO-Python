import sys

IMPOSSIBLE = 1000000

a, b, c, d = map(int, input().split())
if a == b:
    print(1)
    sys.exit()
if (((a + b) == 2 * c) and (c == d)):
    print(2)
    sys.exit()

odd_answer = IMPOSSIBLE
start = a + d + b
if (start == 3 * c):
    odd_answer = 3
else:
    if (start < 3 * c):
        how_far_off = (3 * c) - start
        max_step = (b + d) - 2 * c
    else:
        how_far_off = start - (3 * c)
        max_step = (2 * c) - (a + d)
    if (max_step > 0):
        steps_needed = how_far_off // max_step;
        if (how_far_off % max_step != 0):
            steps_needed += 1
        odd_answer = 3 + 2 * steps_needed

even_answer = IMPOSSIBLE
start = a + d + d + b
if (start == 4 * c):
    odd_answer = 4
else:
    if (start < 4 * c):
        how_far_off = 4 * c - start
        max_step = b + d - 2 * c
    else:
        how_far_off = start - 4 * c
        max_step = 2 * c - (a + d)
    if (max_step > 0):
        steps_needed = how_far_off // max_step;
        if (how_far_off % max_step != 0):
            steps_needed += 1
        even_answer = 4 + 2 * steps_needed
answer = min(odd_answer, even_answer)
if (answer == IMPOSSIBLE):
    answer = 0;
print(answer)