# read input
N = int(input().strip())
messages = input().strip()

# calculate known doubles
known_count = 0
for idx in range(len(messages) - 1):
    if messages[idx] in "BE" and \
            messages[idx] == messages[idx + 1]:
        known_count += 1

consecutive_fs = []  # store all consecutive F strings

# iterate through messages to find F sequences
# examples: BFFFFFB, EFB, BFF, FFB, FFFFF, etc.
i = 0
while i < len(messages):
    if messages[i] == 'F':  # this if statement only applies to the first F in a sequence
        start = i           # start is given the index of the first F in the sequence
        while i < len(messages) and messages[i] == 'F': # immediately finish the sequence of F's
            i += 1  # increment i
        end = i     # give end the value of ending i

        current_string = "" # Build the string with neighboring chars
        if start > 0 and messages[start - 1] in "BE":  # add preceding B/E if exists
            current_string += messages[start - 1]
        current_string += messages[start:end]  # add all the Fs
        if end < len(messages) and messages[end] in "BE":  # add ending B or E if exists
            current_string += messages[end]

        consecutive_fs.append(current_string)  # add the current string to the list
    else:   # just a random B/E
        i += 1  # increment and continue the while loop

# convert F strings to possible double values using the pattern
possibilities = []
for thing in consecutive_fs:
    first = thing[0]          # first char in the F sequence
    last = thing[-1]          # last char in the F sequence
    num_f = thing.count('F')  # count only the F's

    if first == 'F' and last == 'F':    # start and end are F, meaning the string messages is only F's
        possibilities.append([i for i in range(num_f)])
    elif first == 'F' or last == 'F':   # either the start or end is an F
        possibilities.append([i for i in range(num_f + 1)])
    else:   # No F at the start or end of the F sequence
        if first == last:   # if B - B or E - E, same edge chars
            possibilities.append([i for i in range(0, num_f + 2, 2)])
        else:               # if B - E or E - B, different edge chars
            possibilities.append([i for i in range(1, num_f + 2, 2)])

distinct = set()

# do a recursive nested loop for every single possibility
def recursive_nested(number_lists, curr_sum=0, nested_count=0):
    if not number_lists:  # handles empty list edge case
        distinct.add(0)
        return
    if nested_count == len(number_lists) - 1:  # base case on last list
        for num in number_lists[nested_count]:
            distinct.add(curr_sum + num)
        return

    for num in number_lists[nested_count]:  # recursive call
        recursive_nested(number_lists, curr_sum + num, nested_count + 1)

# run this to generate all possibilities
recursive_nested(possibilities)

# print output in correct format
print(len(distinct))
sorted_distinct = sorted(list(map(lambda x: x + known_count, list(distinct))))
for val in sorted_distinct:
    print(val)