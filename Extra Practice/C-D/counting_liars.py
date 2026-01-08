N = int(input())

def read_info():
    s, n = input().split()
    s = True if s == "G" else False
    n = int(n)
    return s, n

P = sorted([read_info() for _ in range(N)], key=lambda x: x[1])

test_vals = [P[0][1]-0.1]
for i in range(N):
    test_vals.append(P[i][1])
    test_vals.append(P[i][1]+0.1)

min_liars =  N
for val in test_vals:
    liars = 0
    for sign, num in P:
        if (val < num) is sign and val != num:
            liars += 1
    min_liars = min(min_liars, liars)

print(min_liars)