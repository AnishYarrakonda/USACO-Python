N, K = map(int, input().strip().split())

base_k_representation = []
while N > 0:
    base_k_representation.insert(0, N % K)
    N //= K
base_k_representation[0] -= 1

pressed = 0
last_idx = len(base_k_representation) - 1
for idx, digit in enumerate(base_k_representation):
    if idx == last_idx:
        pressed += digit
    else:
        pressed += digit + 1

print(pressed)