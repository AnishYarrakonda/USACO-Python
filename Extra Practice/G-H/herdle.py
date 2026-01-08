answer = list(input().strip()) + list(input().strip()) + list(input().strip())
guess  = list(input().strip()) + list(input().strip()) + list(input().strip())

green = 0
yellow = 0

green_indices = []
for i in range(9):
    if answer[i] == guess[i]:
        green += 1
        green_indices.append(i)

used_answer = set(green_indices)
for i in range(9):
    if i in green_indices:
        continue
    for j in range(9):
        if j not in used_answer and guess[i] == answer[j]:
            yellow += 1
            used_answer.add(j)
            break

print(green)
print(yellow)