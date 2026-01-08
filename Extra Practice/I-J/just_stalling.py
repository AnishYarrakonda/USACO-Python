N = int(input().strip())
A = sorted(list(map(int, input().strip().split())))
B = sorted(list(map(int, input().strip().split())))

possible_cows_per_barn = []
for barn_number, barn_height in enumerate(B):
    cows_that_fit = 0
    for cow_height in A:
        if cow_height <= barn_height:
            cows_that_fit += 1
    possible_cows_per_barn.append(cows_that_fit - barn_number)

product = 1
for x in possible_cows_per_barn:
    product *= x
print(product)