def solve():
    # Target distance in cm
    target_d = 6500000

    # Pell equation M^2 - 2D^2 = -1
    # Fundamental solution
    m, d = 1, 1

    # Iterate to find the first d > target_d
    while d <= target_d:
        # Use the recurrence for solutions to x^2 - 2y^2 = -1
        # The next solution is found by multiplying (m + d*sqrt(2)) * (3 + 2*sqrt(2))
        m, d = 3*m + 4*d, 2*m + 3*d

    # Check Case 1: N = M and N % 4 == 1
    # Check Case 2: N = M - 1 and N % 4 == 2
    if m % 4 == 1:
        n = m
    elif (m - 1) % 4 == 2:
        n = m - 1
    else:
        # This part shouldn't be reached for the smallest d > target
        return None

    return n * (n + 1) // 2

print(solve())
