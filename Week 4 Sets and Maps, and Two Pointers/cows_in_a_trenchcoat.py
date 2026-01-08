N, K, J = list(map(int, input().strip().split()))
his = set(list(map(int, input().strip().split())))

total = 1 if J in his else 0

if K >= 2:
    for i in his:
        ii = J - i
        if ii in his and ii > i:
            total += 1

if K >= 3:
    for i in his:
        for ii in his:
            if ii <= i:
                continue
            iii = J - i - ii
            if iii in his and iii > ii:
                total += 1

print(total)