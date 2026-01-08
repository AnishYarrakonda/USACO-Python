N = int(input().strip())
line = [int(input().strip()) for _ in range(N)]
ordered_line = sorted(line)

messed_up_indexes = []
for i in range(N):
    if line[i] != ordered_line[i]:
        messed_up_indexes.append(i)
print(max(0, len(messed_up_indexes)-1))