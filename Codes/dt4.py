def is_palindrome(n):
    """Checks if a number is a palindrome."""
    s = str(n)
    return s == s[::-1]

def find_largest_palindrome():
    max_palindrome = 0
    factors = (0, 0)

    # Iterate through 4-digit numbers from largest to smallest
    for i in range(9999, 999, -1):
        # Optimization: if i * max 3-digit number is less than max_palindrome,
        # we can stop entirely because products will only get smaller.
        if i * 999 <= max_palindrome:
            break

        # Iterate through 3-digit numbers from largest to smallest
        for j in range(999, 99, -1):
            product = i * j

            # Optimization: if current product is smaller than max_palindrome,
            # no need to check smaller j values for this i.
            if product <= max_palindrome:
                break

            if is_palindrome(product):
                max_palindrome = product
                factors = (i, j)

    return max_palindrome, factors

result, (f1, f2) = find_largest_palindrome()
print(f"The largest palindrome is: {result} ({f1} x {f2})")
print(result)
