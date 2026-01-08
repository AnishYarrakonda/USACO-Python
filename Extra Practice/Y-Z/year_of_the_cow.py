# number of cows used for reading the input in a for loop
N = int(input().strip())

# store zodiac animal to their 0-11 number pair
zodiac_to_number = {
    "Ox": 0, "Tiger": 1, "Rabbit": 2, "Dragon": 3,
    "Snake": 4, "Horse": 5, "Goat": 6, "Monkey": 7,
    "Rooster": 8, "Dog": 9, "Pig": 10, "Rat": 11
}

# store all instructions from statements
instructions = []
for _ in range(N):
    words = input().strip().split()                         # split up the words in the phrase
    cow1, cow2 = words[0], words[7]                         # store cow names
    when_dir, zodiac = words[3], words[4]                   # store cow1's zodiac and previous/next
    instructions.append((cow1, cow2, when_dir, zodiac))     # add the tuple to instructions

# save all the cow's by name and their age in a dictionary
ages = {"Bessie": 0} # give bessie any integer age that is a multiple of 12 for reference

# go in order by instruction because cow2 will always be defined no matter what
# cow 2 is always a previously mentioned cow or Bessie who is assigned a reference value
for cow1, cow2, when_dir, zodiac in instructions:
    ref_year = ages[cow2]   # save the reference year
    target_year = zodiac_to_number[zodiac]  # get the target year which is 0-11

    if when_dir == "next":  # if next zodiac year
        diff = (target_year - (ref_year % 12) + 12) % 12  # formula for difference of years for next zodiac year
        if diff == 0:   # since it doesn't make sense for it to be the same year
            diff = 12   # change 0 to 12
        cow1_year = ref_year + diff     # add the difference

    elif when_dir == "previous":  # if previous zodiac year
        diff = ((ref_year % 12) - target_year + 12) % 12  # formula for difference of years for previous zodiac year
        if diff == 0:   # since it doesn't make sense for it to be the same year
            diff = 12   # change 0 to 12
        cow1_year = ref_year - diff     # add the difference

    # add a new key to the dictionary to store the new cows age relative to Bessie
    ages[cow1] = cow1_year

# print the absolute value of the difference since we don't know who is older, Bessie or Elsie
print(abs(ages["Elsie"] - ages["Bessie"]))