t, d, a = map(int, input().split())

def find_num_additions(score, a):
    num_additions = 0
    power_of_ten = 10**d
    while score < t:
        score += score // power_of_ten
        num_additions += 1
        if num_additions > a:
            # In this case we don't need to know the exact number of
            #   additions -- just that it's bigger than a.
            break
    return num_additions

lo = 10**d
hi = 5 * 10**18

while lo != hi:
    mid = (lo + hi) // 2
    num_additions = find_num_additions(mid, a)
    if num_additions > a:
        lo = mid + 1
    else:
        hi = mid

print(lo)