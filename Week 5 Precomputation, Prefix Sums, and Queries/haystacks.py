n, q = list(map(int, input().split()))
his = [0] + list(map(int, input().split()))
pref_sums = [0]
for i in range(1, n+1):
    pref_sums.append(his[i] + pref_sums[-1])
for _ in range(q):
    query = input().split()
    typ = query[0]
    i = int(query[1])
    if typ == 'A':
        t = his[i] + his[i+1]
        half = t // 2
        extra = t % 2
        pref_sums[i] += (half - his[i])
        his[i] = half
        his[i+1] = half + extra
    else:
        j = int(query[2])
        print(pref_sums[j] - pref_sums[i-1])