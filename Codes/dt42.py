import itertools

def solve():
    # Equation: UN * (UN + 1) = DEUX
    # UN is a 2-digit number (10 to 99), DEUX is a 4-digit number (1000 to 9999)
    # UN * (UN + 1) >= 1000 => UN >= 32

    for u in range(1, 10):
        for n in range(10):
            if u == n:
                continue

            un = 10 * u + n
            deux = un * (un + 1)

            if 1000 <= deux <= 9999:
                # Extract digits of DEUX: D, E, U_prime, X
                d = deux // 1000
                e = (deux // 100) % 10
                u_prime = (deux // 10) % 10
                x = deux % 10

                # Check constraints:
                # 1. The 'U' in DEUX must match the 'U' in UN
                # 2. All letters {U, N, D, E, X} must represent distinct digits
                # 3. Leading digit D cannot be 0 (already handled by 1000 range)

                if u == u_prime:
                    digits = {u, n, d, e, x}
                    if len(digits) == 5:
                        return deux

print(solve())
