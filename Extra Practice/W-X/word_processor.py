with open("word.in", "r") as fin:
    N, K = map(int, fin.readline().split())
    essay = fin.readline().split()

lines = []
line = []
chars_on_line = 0

for i in range(N):
    word = essay[i]
    if chars_on_line + len(word) > K:
        lines.append(line)
        line = []
        chars_on_line = 0
    line.append(word)
    chars_on_line += len(word)

lines.append(line)

with open("word.out", "w") as fout:
    for line in lines:
        fout.write(" ".join(line) + "\n")