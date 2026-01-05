import math

def is_square(n):
    """Efficiently checks if an integer is a perfect square."""
    if n < 0: return False
    sqrt_n = int(math.isqrt(n))
    return sqrt_n * sqrt_n == n

def solve():
    """
    Computes S(25000), the sum of perimeters of all Heron envelopes
    with a perimeter <= 25000.

    A Heron envelope consists of a rectangle (L x H) and an isosceles
    triangle (flap) of height h on side L.
    Let u = L/2, v = h, w = L_flap.
    Conditions:
    1. u, H, w are integers.
    2. u^2 + v^2 = w^2 (v=h must be an integer for AC to be integer).
    3. (2u)^2 + H^2 is a square (rectangle diagonal is integer).
    4. u^2 + (H+v)^2 is a square (diagonal AC=CE is integer).
    5. v < H (flap height < rectangle height).
    6. Perimeter P = 2u + 2H + 2w <= 25000.
    """
    limit = 25000
    h_lim = limit // 2

    # Sieve to allow fast prime factorization for divisor generation
    spf = list(range(h_lim + 1))
    for i in range(2, int(h_lim**0.5) + 1):
        if spf[i] == i:
            for j in range(i*i, h_lim + 1, i):
                if spf[j] == j:
                    spf[j] = i

    def get_divisors_of_n2(n):
        """Generates all divisors of n squared."""
        factors = {}
        curr = n
        while curr > 1:
            p = spf[curr]
            cnt = 0
            while curr % p == 0:
                cnt += 1
                curr //= p
            factors[p] = factors.get(p, 0) + 2 * cnt

        divs = [1]
        for p, power in factors.items():
            new_divs = []
            for d in divs:
                p_pow = 1
                for _ in range(power + 1):
                    new_divs.append(d * p_pow)
                    p_pow *= p
            divs = new_divs
        return divs

    total_s = 0
    # u = L/2. Since P > 4u, u goes up to limit/4.
    for u in range(1, limit // 4 + 1):
        u_sq = u * u
        # Find all v such that u^2 + v^2 = w^2
        # (w-v)(w+v) = u^2
        u2_divs = get_divisors_of_n2(u)
        v_list = []
        for d in u2_divs:
            d2 = u_sq // d
            if d2 > d and (d2 - d) % 2 == 0:
                v_list.append((d2 - d) // 2)

        # Find all H such that (2u)^2 + H^2 is a square
        # (diag-H)(diag+H) = (2u)^2
        h_divs = get_divisors_of_n2(2 * u)
        u2_4 = 4 * u_sq
        h_list = []
        for d in h_divs:
            d2 = u2_4 // d
            if d2 > d and (d2 - d) % 2 == 0:
                h_list.append((d2 - d) // 2)

        # Validate all candidate combinations (v, H)
        for v in v_list:
            w = int(math.isqrt(u_sq + v * v))
            for H in h_list:
                # Heron Envelope constraints
                if H > v and u + H + w <= h_lim:
                    # Final diagonal check for AC and CE
                    if is_square(u_sq + (H + v)**2):
                        total_s += 2 * (u + H + w)

    return total_s

print(solve())
