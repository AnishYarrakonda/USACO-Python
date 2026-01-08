# possibilities after distributing one from odd/even to their own group
# odds remaining -> put them in trios for 1 even pair and 1 odd solo
# any number of evens left add to the last group (plus 1)

N = int(input().strip())
id_numbers = list(map(int, input().strip().split()))

even = sum(1 for id_number in id_numbers if id_number % 2 == 0)
odd = sum(1 for id_number in id_numbers if id_number % 2 == 1)

pairs = min(odd, even)
subgroups = pairs * 2

remaining_odd = odd - pairs
remaining_even = even - pairs

if remaining_odd > 0:
    subgroups += (remaining_odd // 3) * 2
    if remaining_odd % 3 == 1:
        subgroups -= 1
    elif remaining_odd % 3 == 2:
        subgroups += 1
else:
    subgroups += 1

print(subgroups)