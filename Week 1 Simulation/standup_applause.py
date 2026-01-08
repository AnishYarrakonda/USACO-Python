n = int(input())
fis = list(map(int, input().split()))

fis.sort()
num_standing = 0

for f in fis:
    if f <= num_standing:
        num_standing += 1
    else:
        break

print(num_standing)