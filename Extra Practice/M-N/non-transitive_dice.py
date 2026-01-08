T = int(input())

def game(dice_A, dice_B):
    A_wins, B_wins = 0, 0
    for roll_1 in dice_A:
        for roll2 in dice_B:
            if roll_1 > roll2:
                A_wins += 1
            elif roll2 > roll_1:
                B_wins += 1
    if A_wins > B_wins:
        return -1
    elif B_wins > A_wins:
        return 1
    else:
        return 0

def simulate():
    for h in range(1, 11):
        for i in range(1, 11):
            for j in range(1, 11):
                for k in range(1, 11):
                    die_C = [h, i, j, k]
                    winner_2, winner_3 = game(die_B, die_C), game(die_C, die_A)
                    if not winner_2 or not winner_3:
                        continue
                    elif winner_1 == winner_2 == winner_3:
                        print("yes")
                        return
    print("no")
    return

for _ in range(T):
    numbers = list(map(int, input().split()))
    die_A, die_B = numbers[0:4], numbers[4:8]
    winner_1 = game(die_A, die_B)
    if not winner_1:
        print("no")
    else:
        simulate()