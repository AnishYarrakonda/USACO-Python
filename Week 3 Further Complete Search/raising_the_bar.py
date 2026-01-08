winning_outcomes = 0
for a in range(4):
    for b in range(6):
        for c in range(8):
            for d in range(10):
                for e in range(12):
                    for f in range(20):
                        if a <= b <= c <= d <= e <= f:
                            winning_outcomes += 1
print(winning_outcomes)