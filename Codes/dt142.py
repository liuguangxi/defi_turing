def solve():
    count = 0
    # Irregular numbers are positive integers not divisible by any of their digits.
    # Note: If a digit is 0, we do not check for divisibility (division by zero).
    for n in range(1, 1000000):
        is_irregular = True
        temp = n
        while temp > 0:
            digit = temp % 10
            temp //= 10
            # If the number is divisible by a non-zero digit, it's not irregular.
            if digit != 0 and n % digit == 0:
                is_irregular = False
                break
        if is_irregular:
            count += 1
    return count

print(solve())
