cowphabet = input().strip()
letters_heard = list(input().strip())

counter = 0
while letters_heard:
    for letter in cowphabet:
        if not letters_heard:
            break
        if letter == letters_heard[0]:
            letters_heard.pop(0)
    counter += 1

print(counter)