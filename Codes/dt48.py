import sys

# Increase the limit for integer to string conversion
# 2013^2013 has approx 6651 digits
if hasattr(sys, 'set_int_max_str_digits'):
    sys.set_int_max_str_digits(10000)

def solve():
    # Calculate the full sum
    total = sum(pow(i, i) for i in range(1, 2014))

    # Return the first 10 digits (most significant)
    return str(total)[:10]

print(solve())
