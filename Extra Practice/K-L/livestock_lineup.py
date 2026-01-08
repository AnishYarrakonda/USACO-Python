ordered_cow_names = ['Beatrice', 'Belinda', 'Bella', 'Bessie', 'Betsy', 'Blue', 'Buttercup', 'Sue']
name_to_number = {ordered_cow_names[i]: str(i) for i in range(8)}
number_to_name = {str(i): ordered_cow_names[i] for i in range(8)}

N = int(input().strip())
pairs = []
for i in range(N):
    words = input().strip().split()
    pairs.append(name_to_number[words[0]] + name_to_number[words[5]])
    pairs.append(name_to_number[words[5]] + name_to_number[words[0]])

best_order = "9"
def nested_for_loop(nested_loops_remaining, current_lineup="", bench="01234567"):
    if nested_loops_remaining == 0:
        for pair in pairs:
            if pair not in current_lineup and pair[::-1] not in current_lineup:
                return
        global best_order
        best_order = min(best_order, current_lineup)
        return
    for remaining in bench:
        nested_for_loop(nested_loops_remaining-1, current_lineup + remaining, bench.replace(remaining, "", 1))

nested_for_loop(8)
for char in best_order:
    print(number_to_name[char], end=" ")