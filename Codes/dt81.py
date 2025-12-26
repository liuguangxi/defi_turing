import math

def solve():
    largest_square = 0
    # Search for n such that n^2 is a 9-digit square number.
    # The range for n is from sqrt(10^8) to sqrt(10^9 - 1).
    start = int(math.ceil(math.sqrt(10**8)))
    end = int(math.floor(math.sqrt(10**9 - 1)))

    for n in range(start, end + 1):
        sq = n * n
        s_sq = str(sq)

        # Avoid squares that end in 0 to prevent leading zeros in the mirrored number.
        if s_sq.endswith('0'):
            continue

        # The mirror of the square number.
        rev_sq = int(s_sq[::-1])

        # The mirror of the square root.
        rev_n = int(str(n)[::-1])

        # Check if the square root of the mirrored square is the mirror of the original root.
        if rev_n * rev_n == rev_sq:
            # Check if both are 9 digits (rev_sq could technically be smaller if sq had trailing zeros,
            # but we filtered those).
            if 100000000 <= rev_sq <= 999999999:
                largest_square = max(largest_square, sq, rev_sq)

    return largest_square

print(solve())
