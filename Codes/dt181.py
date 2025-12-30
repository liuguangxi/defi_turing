import math

def is_pan(n):
    """Checks if a 9-digit number is 1-9 pandigital."""
    if n < 123456789:
        return False
    bits = 0
    while n:
        n, m = divmod(n, 10)
        if m == 0:
            return False
        bits |= (1 << m)
    return bits == 1022  # Binary 1111111110 (bits 1 to 9 set)

# Precompute constants for the approximation of F_k
# F_k ≈ phi^k / sqrt(5)
phi = (1 + 5**0.5) / 2
log_phi = math.log10(phi)
log_sqrt5 = math.log10(5) / 2

f1, f2 = 1, 1
k = 2

while True:
    k += 1
    # Standard iterative step for Fibonacci last 9 digits
    f1, f2 = f2, (f1 + f2) % 1000000000

    # Check if the last nine digits are pandigital (faster check first)
    if is_pan(f2):
        # Calculate approximation of first nine digits using logs
        t = k * log_phi - log_sqrt5
        # The first nine digits of F_k correspond to 10^(fractional_part_of_log + 8)
        first_9 = int(10**(t - int(t) + 8))

        # Check if the first nine digits are pandigital
        if is_pan(first_9):
            print(k)
            break
