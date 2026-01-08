# read inputs
N = int(input())
p = list(map(int, input().split()))
t = list(map(int, input().split()))

# get the differences required to make all temp needed 0
diff = [p[i] - t[i] for i in range(N)]

# pad with leading and trailing zero to calculate deltas
diff.insert(0, 0)
diff.append(0)

# store and fill deltas
deltas = []
for i in range(N+1):
    deltas.append(diff[i+1] - diff[i])

# sum up either positive nums since sum_pos + sum_neg = 0
sum_pos = 0
for num in deltas:
    if num > 0:
        sum_pos += num

# sum_pos = answer
print(sum_pos)