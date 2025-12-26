import math

def solve():
    # Range of 7-digit square roots
    # Lower bound: sqrt(1,000,000) = 1000
    # Upper bound: sqrt(9,999,999) approx 3162.27
    start_root = 3162
    end_root = 1000

    # Iterate from the largest possible square root downwards
    for n in range(start_root, end_root - 1, -1):
        sq = n * n
        s_sq = str(sq)

        # Ensure it is a 7-digit number
        if len(s_sq) != 7:
            continue

        # Check if the square is a palindrome (ABCD CBA)
        if s_sq == s_sq[::-1]:
            # Extracted digits based on the positions of A, B, C, D
            # s[0]=A, s[1]=B, s[2]=C, s[3]=D
            digits = {s_sq[0], s_sq[1], s_sq[2], s_sq[3]}

            # Condition: Two different letters represent two different digits
            # Thus, A, B, C, and D must be distinct digits.
            if len(digits) == 4:
                return sq

print(solve())
