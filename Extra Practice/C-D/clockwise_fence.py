N = int(input().strip())

pair_to_direction = {
    "NE": 1, "NW": -1,
    "ES": 1, "EN": -1,
    "SW": 1, "SE": -1,
    "WN": 1, "WS": -1,
}

def compress_string(s):
    result = [s[0]]
    for char in s[1:]:
        if char != result[-1]:
            result.append(char)
    return ''.join(result)

def calc_fence(fence):
    simple_fence = compress_string(fence)
    total = 0

    L = len(simple_fence)
    for i in range(L):
        a = simple_fence[i]
        b = simple_fence[(i + 1) % L]
        pair = a + b
        total += pair_to_direction.get(pair, 0)

    return total > 0

for _ in range(N):
    if calc_fence(input().strip()):
        print("CW")
    else:
        print("CCW")