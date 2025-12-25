def get_digit(n):
    # n is 1-indexed (d_1 is n=1)
    d = 1        # Current number of digits
    count = 9    # Total digits available for numbers with length 'd'

    # 1. Determine how many digits the number containing the n-th digit has
    while n > d * count:
        n -= d * count
        d += 1
        count *= 10

    # 2. Find the specific number containing the digit
    # (n-1) because we are now offset within the block of d-digit numbers
    num_offset = (n - 1) // d
    actual_num = 10**(d - 1) + num_offset

    # 3. Find the specific digit within that number
    digit_index = (n - 1) % d
    return int(str(actual_num)[digit_index])

def solve():
    product = 1
    # Expression: d_1 * d_10 * ... * d_10^8
    for i in range(9):
        target = 10**i
        digit = get_digit(target)
        if digit == 0: return 0 # Optimization: any zero makes product 0
        product *= digit
    return product

print(solve())
