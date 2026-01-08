import itertools

q, n = map(int, input().split())
g = input()
f1_score = int(input())
f1_list = input()
f2_score = f1_score
f2_list = f1_list
if n == 2:
    f2_score = int(input())
    f2_list = input()

agree_both = 0
agree_f1 = 0
agree_f2 = 0
agree_neither = 0
for i in range(q):
    af1 = (g[i] == f1_list[i])
    af2 = (g[i] == f2_list[i])
    if af1:
        if af2:
            agree_both += 1
        else:
            agree_f1 += 1
    else:
        if af2:
            agree_f2 += 1
        else:
            agree_neither += 1
best_guessie_score = 0

for xb in range(agree_both + 1):
    for xa1 in range(agree_f1 + 1):
        for xa2 in range(agree_f2 + 1):
            for xn in range(agree_neither + 1):
                poss_f1_score = (xb + xa1 + (agree_f2 - xa2) +
                                  (agree_neither - xn))
                if f1_score != poss_f1_score:
                    continue
                poss_f2_score = (xb + (agree_f1 - xa1) +
                                 xa2 + (agree_neither - xn))
                if f2_score != poss_f2_score:
                    continue
                best_guessie_score = max(best_guessie_score,
                                         xb + xa1 + xa2 + xn)

print(best_guessie_score)