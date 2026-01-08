N, Q = map(int, input().split())
keywords = input().split()
assert N % 2 == 1 and len(keywords) == N

for i in range(0, N, 2):
    keywords[i] = keywords[i] == "true"

lowest_r = float("inf")
highest_l = -1

r = 0
while r < N:
    l = r
    group_result = keywords[l]
    while r + 1 < N and keywords[r + 1] == "and":
        r += 2
        group_result &= keywords[r]
    if group_result:
        lowest_r = min(lowest_r, r)
        highest_l = max(highest_l, l)
    r += 2

exists_false_left_of = [False] * N
for i in range(2, N, 2):
    if keywords[i - 1] == "or":
        continue
    exists_false_left_of[i] = exists_false_left_of[i - 2] or keywords[i - 2] == False

exists_false_right_of = [False] * N
for i in reversed(range(0, N - 1, 2)):
    if keywords[i + 1] == "or":
        continue
    exists_false_right_of[i] = exists_false_right_of[i + 2] or keywords[i + 2] == False

answers = []
for _ in range(Q):
    l, r, result = input().split()
    l = int(l) - 1
    r = int(r) - 1
    result = result == "true"
    assert l % 2 == 0 and r % 2 == 0
    eval_result = lowest_r < l or r < highest_l
    if not (exists_false_left_of[l] or exists_false_right_of[r]):
        eval_result |= result
    answers.append(result == eval_result)

print("".join(map(lambda x: {False: "N", True: "Y"}[x], answers)))