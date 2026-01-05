import math

def solve():
    def get_n_string(a, b, c, n):
        return str(a) + str(b).zfill(n) + str(c).zfill(n)

    for n in range(2, 10):
        k = 10**n + 1
        mod = 2018
        g = math.gcd(k, mod)
        m = mod // g

        for a in range(10**(n-1), 10**n):
            target = (-k * (10**n) * a) % mod
            if target % g != 0:
                continue

            c0 = (target // g * pow(k // g, -1, m)) % m

            max_c = 10**n - 1 - a
            c = c0
            while c <= max_c:
                # B = A + C
                b = a + c
                # N = a * 10^(2n) + b * 10^n + c
                n_val = a * 10**(2*n) + b * 10**n + c
                s = get_n_string(a, b, c, n)
                if "2018" in s:
                    return n_val
                c += m

    return None

print(solve())
