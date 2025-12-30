import itertools

def solve():
    # Letters involved: G, R, A, I, N, S, B, L, E (9 distinct letters)
    # Equation: k * GRAIN = SABLE
    # GRAIN = G*10000 + R*1000 + A*100 + I*10 + N
    # SABLE = S*10000 + A*1000 + B*100 + L*10 + E

    letters = ('G', 'R', 'A', 'I', 'N', 'S', 'B', 'L', 'E')

    # Range of k:
    # Smallest 5-digit GRAIN is 10234.
    # Largest 5-digit SABLE is 98765.
    # k * 10234 <= 98765 => k <= 9.65
    for k in range(9, 1, -1):
        sable_values = []
        # Optimization: Iterate over G, R, A, I, N (G != 0)
        # Then calculate SABLE = k * GRAIN
        # Check if SABLE matches S, A, B, L, E pattern and distinct letters
        for p in itertools.permutations(range(10), 5):
            g, r, a, i, n = p
            if g == 0: continue

            grain = g * 10000 + r * 1000 + a * 100 + i * 10 + n
            sable = k * grain

            if sable < 10000 or sable > 99999: continue

            s_val = sable // 10000
            a_val = (sable // 1000) % 10
            b_val = (sable // 100) % 10
            l_val = (sable // 10) % 10
            e_val = sable % 10

            # Constraints:
            # 1. 'A' in SABLE must match 'A' in GRAIN
            if a_val != a: continue
            # 2. S != 0
            if s_val == 0: continue

            # Check distinctness of the 9 letters
            current_digits = {g, r, a, i, n, s_val, b_val, l_val, e_val}
            if len(current_digits) == 9:
                sable_values.append(sable)

        if sable_values:
            return sum(sable_values)
    return None

print(solve())
