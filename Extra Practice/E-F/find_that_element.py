N, Q = map(int, input().split())
arr = list(map(int, input().split()))

indices = {arr[i]: i+1 for i in range(N)}

for _ in range(Q):
    print(indices[int(input())])