N = int(input())
S = input()

count = 0
for i in range(N):
    for j in range(i+1, N):
        if S[i] < S[j]:
            count += 1

print(count)