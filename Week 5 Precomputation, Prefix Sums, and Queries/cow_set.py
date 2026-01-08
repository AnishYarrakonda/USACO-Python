T, D = map(int, input().split())
table = input().split()
table_as_set = set(table)
deck = input().split()
pair_to_single = {"CO":"W", "OC":"W",
                  "CW":"O", "WC":"O",
                  "OW":"C", "WO":"C"}

def get_third(first, second):
    third = ""
    for idx in range(4):
        if first[idx] == second[idx]:
            third += first[idx]
        else:
            third += pair_to_single[first[idx]+second[idx]]
    return third

def check_third(first, second, set_x):
    third = ""
    for idx in range(4):
        if first[idx] == second[idx]:
            third += first[idx]
        else:
            third += pair_to_single[first[idx]+second[idx]]
    return third in set_x

cow_to_sets = {}


for d_cow in deck:
    count = 0
    for t_cow in table:
        count += check_third(d_cow, t_cow, table_as_set)
    cow_to_sets[d_cow] = count//2

max_inc = 0

for i in range(D):
    for j in range(i+1, D):
        for k in range(j+1, D):
            cow1, cow2, cow3 = deck[i], deck[j], deck[k]

            total_sets = cow_to_sets[cow1] + cow_to_sets[cow2] + cow_to_sets[cow3]

            total_sets += check_third(cow1, cow2, table_as_set)
            total_sets += check_third(cow2, cow3, table_as_set)
            total_sets += check_third(cow1, cow3, table_as_set)

            total_sets += get_third(cow1, cow2) == cow3

            max_inc = max(max_inc, total_sets)

print(max_inc)