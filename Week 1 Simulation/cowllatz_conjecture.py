n = int(input())
numbers = set()
while n != 1:
    if n % 2 == 0:
        n /= 2
    else:
        n = n * 3 + 1
    numbers.add(n)
print(len(numbers) + 1)