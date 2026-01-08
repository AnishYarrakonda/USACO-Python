def solve(p):
    letter_counts = {}
    for letter in p:
        if letter not in letter_counts:
            letter_counts[letter] = 0
        letter_counts[letter] += 1
    digit_counts = [0]*10
    for key_letter, digit_word, digit in (('Z', 'ZERO', 0),
                                          ('W', 'TWO', 2),
                                          ('U', 'FOUR', 4),
                                          ('X', 'SIX', 6),
                                          ('G', 'EIGHT', 8),
                                          ('O', 'ONE', 1),
                                          ('H', 'THREE', 3),
                                          ('F', 'FIVE', 5),
                                          ('S', 'SEVEN', 7),
                                          ('I', 'NINE', 9)):
        if key_letter in letter_counts and letter_counts[key_letter] > 0:
            letter_dict = {}
            for letter in digit_word:
                if letter not in letter_dict:
                    letter_dict[letter] = 0
                letter_dict[letter] += 1
            key_letter_count = letter_counts[key_letter]
            digit_counts[digit] = key_letter_count
            for k, v in letter_dict.items():
                letter_counts[k] -= key_letter_count * v
    ans = ''
    if digit_counts[0] != 0:
        for dd in range(1, 10):
            if digit_counts[dd] != 0:
                ans += str(dd)
                digit_counts[dd] -= 1
                break
    for d in range(10):
        ans += str(d)*digit_counts[d]
    return ans

p = input()
print(solve(p))