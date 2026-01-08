N, K = map(int, input().strip().split())
cis = list(map(int, input().strip().split()))

final_card = [0] * N

for i in range(N - 1, -1, -1):
    jump_to = i + cis[i]
    if jump_to >= N:
        final_card[i] = i
    else:
        final_card[i] = final_card[jump_to]

bessie_final = final_card[0]
x = sum(1 for i in range(K) if final_card[i] == bessie_final)
print(x)