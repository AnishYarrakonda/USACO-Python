N = int(input())
A = list(map(int, input().split()))
K = int(input())
recipes = [None] * N

for _ in range(K):
    recipe = list(map(int, input().split()))
    L = recipe[0] - 1  # Convert to 0-indexed
    M = recipe[1]
    recipes[L] = [recipe[i] - 1 for i in range(2, 2 + M)]

def can_make(metal):
    # If we already have this metal, just use it
    if A[metal] > 0:
        A[metal] -= 1
        return True

    # If no recipe exists, we can't make it
    if recipes[metal] is None:
        return False

    # Try to make all components from the recipe
    for sub_metal in recipes[metal]:
        if not can_make(sub_metal):
            return False

    return True


ans = 0
while can_make(N - 1):
    ans += 1

print(ans)