def solve():
    n = 20142014

    # Each diagonal 'd' (d=1, 2, 3, ...) contains 'd' numbers.
    # The total count of numbers in the first 'k' diagonals is T(k) = k*(k+1)/2.
    # We find 'k' such that T(k) < n <= T(k+1).
    k = int((2 * n)**0.5)
    while k * (k + 1) // 2 < n:
        k += 1
    while k * (k - 1) // 2 >= n:
        k -= 1

    # 'd' is the diagonal containing 'n'.
    d = k
    # 'pos' is the position of 'n' within its diagonal (from 1 to 'd').
    base = (d - 1) * d // 2
    pos = n - base

    # Observation of the zig-zag pattern:
    # Diagonal d=1: (1,1) -> row 1
    # Diagonal d=2: (1,2), (2,1) -> rows 1, 2
    # Diagonal d=3: (3,1), (2,2), (1,3) -> rows 3, 2, 1
    # Diagonal d=4: (1,4), (2,3), (3,2), (4,1) -> rows 1, 2, 3, 4
    # Diagonal d=5: (5,1), (4,2), (3,3), (2,4), (1,5) -> rows 5, 4, 3, 2, 1

    # Rule:
    # If d is odd: rows go from d down to 1. row = d - pos + 1
    # If d is even: rows go from 1 up to d. row = pos

    if d % 2 == 1:
        row = d - pos + 1
    else:
        row = pos

    return row

print(solve())
