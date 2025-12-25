def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solve():
    # Precompute primes for b up to 1500
    b_primes = [b for b in range(2, 1500) if is_prime(b)]

    max_n = 0
    best_product = 0

    for b in b_primes:
        # a must be odd if b > 2 to ensure 1 + a + b is odd (and potentially prime)
        for a in range(-1499, 1500):
            n = 0
            while True:
                val = n*n + a*n + b
                if val < 2 or not is_prime(val):
                    break
                n += 1

            if n > max_n:
                max_n = n
                best_product = a * b

    return best_product

print(solve())
