N = int(input().strip())
ans = list(map(int, input().strip().split()))

even = sorted(ans[::2])
odd = sorted(ans[1::2])

sorted_ans = []
for i in range(N):
    if i % 2 == 0:
        sorted_ans.append(even[i//2])
    else:
        sorted_ans.append(odd[i//2])

for i in range(N-1):
    if sorted_ans[i] > sorted_ans[i+1]:
        print(i)
        break
else:
    print(N)