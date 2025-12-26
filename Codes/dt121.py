import itertools

def solve():
    # A magic square in this context is a 3x3 grid (a..i)
    # a b c
    # d e f
    # g h i
    # such that the four 2x2 sub-squares have the same sum S.

    count = 0
    # The set of numbers is 1 to 9.
    nums = range(1, 10)

    # Iterate through all permutations of 1..9
    # 9! = 362,880, which is small enough for a brute-force approach.
    for p in itertools.permutations(nums):
        a, b, c, d, e, f, g, h, i = p

        # Calculate sums of the four 2x2 squares
        s1 = a + b + d + e
        s2 = b + c + e + f
        if s1 != s2:
            continue

        s3 = d + e + g + h
        if s1 != s3:
            continue

        s4 = e + f + h + i
        if s1 != s4:
            continue

        count += 1

    return count

print(solve())
