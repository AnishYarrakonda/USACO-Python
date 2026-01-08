N = int(input().strip())
line = list(map(lambda x: 1 if x == 'H' else 0, list(input().strip())))

lonely_photos = 0
for idx, char in enumerate(line):
    if char:
        a, b = 0, 0
        while idx - a - 1 >= 0 and not line[idx - a - 1]:
            a += 1
        while idx + b + 1 < N and not line[idx + b + 1]:
            b += 1
        lonely_photos += (a+1) * (b+1) - 1 - min(a, 1) - min(b, 1)

line = list(map(lambda x: int(not x), line))

for idx, char in enumerate(line):
    if char:
        a, b = 0, 0
        while idx - a - 1 >= 0 and not line[idx - a - 1]:
            a += 1
        while idx + b + 1 < N and not line[idx + b + 1]:
            b += 1
        lonely_photos += (a+1) * (b+1) - 1 - min(a, 1) - min(b, 1)

print(lonely_photos)