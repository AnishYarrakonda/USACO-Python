total = 0
for a in range(2, 201):
  for b in range(a+1, 201):
    for c in range(b+1, 201):
      if a**2 + b**2 == c**2:
        total += 1
print(total)