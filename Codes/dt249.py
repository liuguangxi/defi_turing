def solve():
    # Let n be a k-digit integer.
    # Writing a 1 to the left and right of n: 10^(k+1) + 10n + 1
    # Condition: 10^(k+1) + 10n + 1 = 99n => 89n = 10^(k+1) + 1
    # Thus 10^(k+1) must be congruent to -1 modulo 89.

    p = 89
    # Find the smallest m such that 10^m = -1 (mod 89)
    m = next(i for i in range(1, 100) if pow(10, i, p) == p - 1)
    # Find the order d of 10 mod 89
    d = next(i for i in range(1, 100) if pow(10, i, p) == 1)

    # The number of digits k satisfies k+1 = m + j*d for j >= 0.
    # So k = (m-1) + j*d.
    # First term U = m-1, common difference R = d.
    U = m - 1
    R = d

    # Elements n_k = (10^(k+1) + 1) / 89.
    # n_k - n_U = (10^(k+1) - 10^m) / 89 = 10^m * (10^(j*d) - 1) / 89.
    # Since (10^d - 1) / 89 is an integer not divisible by 10,
    # the suffix of length P shared by all n_k is of length m.
    # Thus P = m.
    P = m

    # A is the constant residue modulo 10^P.
    # Since n_U = (10^22 + 1) / 89 is a 21-digit number, A = n_U.
    A = (10**m + 1) // p

    # Calculate A * P * R * U and extract the last 12 digits.
    print(f"A = {A}, P = {P}, R = {R}, U = {U}")
    result = A * P * R * U
    print(str(result)[-12:])

solve()
