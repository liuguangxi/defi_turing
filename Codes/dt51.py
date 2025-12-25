import itertools

def solve():
    digits = [0, 1, 3, 4, 5, 6, 7, 8, 9]
    # Letters: A, R, G, N, D, E, U, L, I
    # Constraints:
    # A, E, G != 0
    # G = A + 1
    # D + R = N + 10*c1
    # N + E + c1 = I + 10*c2
    # A + L + c2 = D + 10*c3
    # G + U + c3 = L + 10*c4
    # R + E + c4 = U + 10

    for p in itertools.permutations(digits):
        # Mapping: A, R, G, N, D, E, U, L, I
        A, R, G, N, D, E, U, L, I = p

        if A == 0 or E == 0 or G == 0:
            continue

        if G != A + 1:
            continue

        c1, n_rem = divmod(D + R, 10)
        if n_rem != N: continue

        c2, i_rem = divmod(N + E + c1, 10)
        if i_rem != I: continue

        c3, d_rem = divmod(A + L + c2, 10)
        if d_rem != D: continue

        c4, l_rem = divmod(G + U + c3, 10)
        if l_rem != L: continue

        if R + E + c4 == U + 10:
            # Check if 0 is used (always true since we use all digits)
            # Check if 2 is used (always false since 2 is not in digits)
            argand = A*100000 + R*10000 + G*1000 + A*100 + N*10 + D
            euler = E*10000 + U*1000 + L*100 + E*10 + R
            # Wait, the word "ARGAND" might be just letters?
            # Let's re-read the cryptarithm carefully.
            # ARGAND
            # EULER
            # GULDIN
            # A, R, G, A, N, D? No, "ARGAND" usually means distinct digits for distinct letters unless stated.
            # R-G-A-N-D vs A-R-G-A-N-D
            # The word is ARGAND.

            val_argand = A*100000 + R*10000 + G*1000 + A*100 + N*10 + D
            val_euler = E*10000 + U*1000 + L*100 + E*10 + R
            val_guldin = G*100000 + U*10000 + L*1000 + D*100 + I*10 + N

            if val_argand + val_euler == val_guldin:
                return val_guldin

print(solve())
