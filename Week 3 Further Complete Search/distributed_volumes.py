# Test for small Ns to try and see a pattern:


def easy_test_case(N):
    greatest_bessie_total = 0
    for number in range(1 << N):
        bessie_total = 0
        essie_total = 0
        bessie_books = 0
        for i in range(N):
            if (number >> i) & 1:
                bessie_total += i + 1
                bessie_books += 1
            else:
                essie_total += i + 1
        if bessie_total == essie_total:
            greatest_bessie_total = max(greatest_bessie_total, bessie_books)
    return bool(greatest_bessie_total), greatest_bessie_total

for n in range(1, 25):
    print(n, easy_test_case(n))


# Output

"""
1 (False, 0)
2 (False, 0)
3 (True, 2)
4 (True, 2)
5 (False, 0)
6 (False, 0)
7 (True, 4)
8 (True, 5)
9 (False, 0)
10 (False, 0)
11 (True, 7)
12 (True, 8)
13 (False, 0)
14 (False, 0)
15 (True, 10)
16 (True, 11)
17 (False, 0)
18 (False, 0)
19 (True, 13)
20 (True, 14)
21 (False, 0)
22 (False, 0)
23 (True, 16)
24 (True, 16)
"""


import math

T = int(input())
for _ in range(T):
    N, X = map(int, input().split())

    if N % 4 == 0 or N % 4 == 3:
        print("POSSIBLE")
        if X == 2:
            target = N * (N + 1) // 4
            bessie_books = int((-1 + (1 + 8 * target) ** 0.5) // 2)
            print(bessie_books)
    else:
        print("IMPOSSIBLE")