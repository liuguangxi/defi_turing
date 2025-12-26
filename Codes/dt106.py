from itertools import permutations

def solve():
    # C=1, D=0, X=9 because (3-digit + 2-digit) >= 1000 implies C=1, D=0, X=9.
    # Remaining digits for {Y, Z, A, B, E, F, G} are {2, 3, 4, 5, 6, 7, 8}.
    remaining_digits = [2, 3, 4, 5, 6, 7, 8]

    for p in permutations(remaining_digits):
        Y, Z, A, B, E, F, G = p

        xyz = 900 + 10 * Y + Z
        ab = 10 * A + B
        cdef = 1000 + 10 * E + F
        bga = 100 * B + 10 * G + A

        # Verify both equations of the cryptarithm
        if xyz + ab == cdef and xyz - ab == bga:
            return xyz * ab

print(solve())
