t = int(input())
for _ in range(t):
    v, n = list(map(int, input().split()))
    ls = list(map(int, input().split()))
    if len(ls) == 1:
        print("INCORRECT" if (v == ls[0]) else "CORRECT")
    elif (v not in ls and v > ls[0]) or (v == ls[-1]):
        print("RUNS FOREVER")
    else:
        print("CORRECT")