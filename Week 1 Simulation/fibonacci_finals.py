def fib_mod(n, mod):
    if n == 0:
        return (0, 1)
    a, b = fib_mod(n >> 1, mod)
    c = (a * ((b * 2 - a) % mod)) % mod
    d = (a * a + b * b) % mod
    return (c, d) if n % 2 == 0 else (d, (c + d) % mod)

def final_fib(j0, j1, n, k):
    mod = 10 ** k
    fn, fn1 = fib_mod(n, mod)
    fnm1 = (fn1 - fn) % mod
    return (j0 * fnm1 + j1 * fn) % mod

first, second, n1, k1 = map(int, input().split())
print(final_fib(first, second, n1, k1))