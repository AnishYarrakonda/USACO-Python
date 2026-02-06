import itertools

ALL_PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

a, b, c, d = map(int, input().split())
primes = []
for p in ALL_PRIMES:
    if a <= p <= b:
        primes.append(p)

num_innocent = d - c + 1
for which_to_take in itertools.product([True, False], repeat=len(primes)):
    prod = 1
    count = 0
    for i in range(len(primes)):
        if which_to_take[i]:
            prod *= primes[i]
            count += 1
    if count == 0:
        continue
    num_multiples = d // prod - (c - 1) // prod
    pie_multiplier = 1 if (count % 2 == 0) else -1
    num_innocent += pie_multiplier * num_multiples

print(num_innocent)