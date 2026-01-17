T = int(input())
MOD = 2**64-59

for _ in range(T):
    S = input()
    i = 0

    running1 = 0
    while (i < len(S) // 2):
        running1 = running1 * 26 + ord(S[i]) - 64
        running1 %= MOD
        i += 1
    
    running2 = 0
    while (i < len(S)):
        running2 = running2 * 26 + ord(S[i]) - 64
        running2 %= MOD
        i += 1
    
    print("YES" if running1 + 1 == running2 else "NO")