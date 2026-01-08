N = int(input())
blocks = [input() for _ in range(4)]
words = [input() for _ in range(N)]

def is_possible(word):
    all_options = []
    for letter in word:
        letter_options = []
        for block in blocks:
            if letter in block:
                letter_options.append(block)
        if not letter_options:
            return False
        all_options.append(letter_options)

    while all_options:
        least_choices = min(all_options, key=len)
        used = least_choices[0]
        all_options.remove(least_choices)
        for letter_options in all_options:
            if used in letter_options:
                letter_options.remove(used)
                if not letter_options:
                    return False

    return True

for string in words:
    if is_possible(string):
        print("YES")
    else:
        print("NO")