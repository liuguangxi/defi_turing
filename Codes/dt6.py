import math
import sys

# Increase the limit for integer-to-string conversion
# 2013! has approximately 5,777 digits
sys.set_int_max_str_digits(10000)

def solve_factorial_digit_sum(n):
    # Calculate n! (e.g., 2013!)
    fact_result = math.factorial(n)

    # Convert to string and sum each digit
    digit_sum = sum(int(digit) for digit in str(fact_result))

    return digit_sum

n = 2013
result = solve_factorial_digit_sum(n)
print(result)
