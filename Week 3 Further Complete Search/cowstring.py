N, S = input().strip().split()
N = int(N)
cow_letters = ["C", "O", "W"]
valid_cow_strings = 0

def recursive_nested(nested_loops_remaining, cow_string):
    if nested_loops_remaining == 0:
        if S in cow_string:
            return
        global valid_cow_strings
        valid_cow_strings += 1
        return
    for letter in cow_letters:
        if S in cow_string:
            break
        recursive_nested(nested_loops_remaining-1, cow_string+letter)

recursive_nested(N, "")
print(valid_cow_strings)