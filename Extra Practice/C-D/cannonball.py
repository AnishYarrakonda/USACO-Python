N, S = map(int, input().split())
S -= 1
Q, V = [], []

for _ in range(N):
    q, v = map(int, input().split())
    Q.append(q)
    V.append(v)

power = 1
broken_targets = set()
jump_pad_zero_states = set()
while 0 <= S < N:
    if Q[S]:
        if abs(power) >= V[S]:
            broken_targets.add(S)
    else:
        direction = 1 if power > 0 else -1
        power = -(power + (direction * V[S]))
        if V[S] == 0:
            state = (S, power)
            if state in jump_pad_zero_states:
                break
            else:
                jump_pad_zero_states.add(state)
    S += power

print(len(broken_targets))