def solve():
    # Multiplicand: M = A2BCD (5 digits, 2 at index 1)
    # Multiplier:   X = EF (2 digits)
    # Product:      P = 2222GH (6 digits, 2 at index 0, 1, 2, 3)
    # Rule: "No others" means all A, B, C, D, E, F, G, H != 2.

    max_multiplicand = 0

    # Product range: 222200 to 222299
    for p in range(222299, 222199, -1):
        s_p = str(p)
        # G and H (indices 4, 5) must not be 2
        if s_p[4] == '2' or s_p[5] == '2':
            continue

        # Check all 2-digit divisors X = EF
        for x in range(10, 100):
            if p % x == 0:
                m = p // x
                s_m = str(m)
                s_x = str(x)

                # M must be 5 digits
                if len(s_m) != 5:
                    continue

                # Multiplicand constraints: _ 2 _ _ _
                # Index 1 must be '2', others must not be '2'
                m_cond = (s_m[1] == '2' and
                          s_m[0] != '2' and
                          s_m[2] != '2' and
                          s_m[3] != '2' and
                          s_m[4] != '2')

                # Multiplier constraints: _ _ (no '2')
                x_cond = (s_x[0] != '2' and s_x[1] != '2')

                if m_cond and x_cond:
                    if m > max_multiplicand:
                        max_multiplicand = m

    return max_multiplicand

print(solve())
