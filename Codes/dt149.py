def solve():
    # We are looking for an integer divisor of 100,000,000.
    # Let target = 100,000,000.
    # Let divisor be D, quotient be Q, and remainder be R.
    # The requirement is that the set of digits in D, Q, and R must be identical.

    target = 100000000
    # The divisor must be smaller than the target.
    # We loop through possible divisors to find one matching the criteria.
    for divisor in range(1, target):
        quotient = target // divisor
        remainder = target % divisor

        # Ensure quotient and remainder are valid for digit set comparison.
        if quotient == 0:
            continue

        # Extract the set of digits used in each number.
        digits_divisor = set(str(divisor))
        digits_quotient = set(str(quotient))
        digits_remainder = set(str(remainder))

        # Check if all three numbers use exactly the same set of digits.
        if digits_divisor == digits_quotient == digits_remainder:
            # We are looking for the possibility other than 91,810.
            if divisor != 91810:
                return divisor

# Solve and print the divisor
print(solve())
