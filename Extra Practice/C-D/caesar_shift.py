S = input()
K = int(input())

alphabet = {chr(97 + i): chr(97 + (i + K) % 26) for i in range(26)}

new_S = []
for char in S:
    new_S.append(alphabet[char])

print("".join(new_S))