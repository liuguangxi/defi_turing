def solve():
    """
    Finds the smallest positive integer for which the proportion of bouncing
    numbers (neither non-decreasing nor non-increasing) first reaches or
    exceeds 99.9%.
    """
    n = 0
    non_bouncy = 0

    # We iterate through integers starting from 1.
    # Non-bouncy numbers are those where digits are either
    # non-decreasing (ascending) or non-increasing (descending).
    # A number is bouncing if it has both an 'increase' and a 'decrease'.
    while True:
        n += 1
        s = str(n)
        inc = dec = False

        # Check if the number is bouncy by looking for direction changes.
        # This one-pass check is faster than sorting or separate direction checks.
        for i in range(len(s) - 1):
            if s[i] < s[i+1]:
                inc = True
            elif s[i] > s[i+1]:
                dec = True

            # If it has both increases and decreases, it is a bouncing number.
            if inc and dec:
                break
        else:
            # The 'else' block executes if the loop was not broken (i.e., not bouncy).
            non_bouncy += 1

        # The proportion condition: bouncy / n >= 0.999
        # Which is equivalent to: (n - non_bouncy) / n >= 999 / 1000
        # 1000 * (n - non_bouncy) >= 999 * n
        # 1000 * n - 1000 * non_bouncy >= 999 * n
        # n >= 1000 * non_bouncy
        if n >= 1000 * non_bouncy:
            return n

print(solve())
