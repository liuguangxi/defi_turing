def is_binary_palindrome(n):
    # bin(n) returns '0b...'
    s = bin(n)[2:]
    return s == s[::-1]

def solve():
    total_sum = 0
    limit = 10_000_000

    # Generate all decimal palindromes up to 10 million
    for length in range(1, 8):
        # A palindrome of length 'length' is determined by its first ceil(length/2) digits
        half_len = (length + 1) // 2
        start = 10**(half_len - 1)
        end = 10**half_len

        for i in range(start, end):
            s = str(i)
            # Create palindrome by mirroring
            if length % 2 == 0:
                # Even length: e.g., 12 -> 1221
                pal_str = s + s[::-1]
            else:
                # Odd length: e.g., 12 -> 121
                pal_str = s + s[:-1][::-1]

            n = int(pal_str)

            if n >= limit:
                continue

            # Condition: Must be odd and binary palindrome
            if n % 2 != 0 and is_binary_palindrome(n):
                total_sum += n

    return total_sum

print(solve())
