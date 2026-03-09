T, k = map(int, input().split())

case_to_letter = {
    ("M", True): "O",
    ("M", False): "M",
    ("O", True): "M",
    ("O", False): "O"
}

for _ in range(T):
    N = int(input())
    moo = input()

    print("YES")

    if k == 0:
        continue

    flips = 0
    backwards_moo = []

    for i in range(N-1, -1, -1):
        letter = case_to_letter[(moo[i], flips & 1)]
        backwards_moo.append(letter)
        flips += letter == "O"

    print("".join(reversed(backwards_moo)))