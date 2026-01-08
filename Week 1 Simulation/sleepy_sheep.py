def sleepy_sheep(n):
    if n == 0:
        return -1
    seen = set()
    number = 0
    while len(seen) < 10:
        number += n
        for digit in str(number):
            seen.add(digit)
    return number

real_n = int(input())
print(sleepy_sheep(real_n))