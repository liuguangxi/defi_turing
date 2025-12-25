def solve():
    # Equation: SIX^2 = TROIS
    # Range of SIX: 100^2 = 10000 (min 5-digit), sqrt(99999) approx 316 (max 5-digit)
    for six in range(100, 317):
        trois = six * six
        s_six = str(six)
        s_trois = str(trois)

        # Length check
        if len(s_trois) != 5:
            continue

        # Mapping letters
        S = int(s_six[0])
        I = int(s_six[1])
        X = int(s_six[2])

        T = int(s_trois[0])
        R = int(s_trois[1])
        O = int(s_trois[2])
        I_prime = int(s_trois[3])
        S_prime = int(s_trois[4])

        # Check consistent letters
        if I == I_prime and S == S_prime:
            # Check unique digits
            digits = {S, I, X, T, R, O}
            if len(digits) == 6:
                return trois

print(solve())
