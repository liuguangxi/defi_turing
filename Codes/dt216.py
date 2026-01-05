def is_palindrome(n):
    """Checks if a number is a palindrome."""
    s = str(n)
    return s == s[::-1]

def solve():
    """
    Calculates the sum of squares of natural numbers 0^2 + 1^2 + 2^2 + ...
    Stops when the square of a palindrome (n >= 10) is added and the total sum
    is also a palindrome.
    """
    total_sum = 0
    n = 0
    while True:
        total_sum += n * n
        # Trigger condition: n must be a palindrome with at least two digits.
        if n >= 10 and is_palindrome(n):
            # Stopping condition: current sum must be a palindrome.
            if is_palindrome(total_sum):
                return total_sum
        n += 1

print(solve())
