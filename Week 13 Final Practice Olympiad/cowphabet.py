import math

def kth_permutation(letters, k):
    if not letters:
        return ""
    n = len(letters)
    fact = math.factorial(n - 1)
    index = (k - 1) // fact
    chosen = letters.pop(index)
    k -= index * fact
    return chosen + kth_permutation(letters, k)

N, K = map(int, input().split())
alphabet = [chr(65 + i) for i in range(N)]
print(kth_permutation(alphabet, K))