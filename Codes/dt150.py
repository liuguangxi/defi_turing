import math
from itertools import product

def solve():
    # 1. Precompute Primes and HCNs up to 1,000,000
    limit = 1000000
    is_prime = [True] * limit
    is_prime[0] = is_prime[1] = False
    divisors = [0] * limit
    for i in range(1, limit):
        for j in range(i, limit, i):
            divisors[j] += 1
            if i > 1 and j > i:
                is_prime[j] = False

    # Identify Highly Composite Numbers (HCNs)
    hcn_list = []
    max_d = 0
    for i in range(1, limit):
        if divisors[i] > max_d:
            max_d = divisors[i]
            if i >= 100000:
                hcn_list.append(i)

    # 2. Identify prime cubes p^3 < 1,000,000
    prime_cubes = [p**3 for p in range(2, 100) if is_prime[p]]

    def has_p3(n):
        return any(n % pc == 0 for pc in prime_cubes)

    # 3. Filter Row F (HCN + Divisibility by all k < F^(1/5))
    lcm_table = [1] * 17
    for i in range(1, 17):
        lcm_table[i] = (lcm_table[i-1] * i) // math.gcd(lcm_table[i-1], i)

    possible_F = []
    for f in hcn_list:
        k_max = int(f**0.2 - 1e-9)
        if f % lcm_table[k_max] == 0:
            possible_F.append([int(d) for d in str(f)])

    # 4. Precompute 6-digit 5th powers as digit lists
    powers = [[int(d) for d in str(x**5)] for x in range(10, 16)]

    # 5. Grid Search
    # Space: 6 (F) * 6^5 (A-E) = 46,656 iterations.
    for f_row in possible_F:
        for rA, rB, rC, rD, rE in product(powers, repeat=5):
            # rows: A, B, C, D, E, F
            grid = [rA, rB, rC, rD, rE, f_row]

            # Vertical column checks
            # Col 0 (a): divisible by 19
            c0 = sum(grid[i][0] * 10**(5-i) for i in range(6))
            if c0 % 19 != 0: continue

            # Col 1 (b): divisible by 37 and p^3
            c1 = sum(grid[i][1] * 10**(5-i) for i in range(6))
            if c1 % 37 != 0 or not has_p3(c1): continue

            # Col 2 (c): divisible by 7
            c2 = sum(grid[i][2] * 10**(5-i) for i in range(6))
            if c2 % 7 != 0: continue

            # Col 3 (d): prime number
            c3 = sum(grid[i][3] * 10**(5-i) for i in range(6))
            if not is_prime[c3]: continue

            # Col 4 (e): divisible by 4 and p^3
            c4 = sum(grid[i][4] * 10**(5-i) for i in range(6))
            if c4 % 4 != 0 or not has_p3(c4): continue

            # Col 5 (f): divisible by 19
            c5 = sum(grid[i][5] * 10**(5-i) for i in range(6))
            if c5 % 19 != 0: continue

            # Found the grid: Extract the yellow diagonal digits
            print("Grid:")
            for row in grid: print(row)
            return "".join(str(grid[i][i]) for i in range(6))

print(solve())
