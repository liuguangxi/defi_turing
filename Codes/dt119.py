def count_divisors_factorial(n):
    # Prime factorization of n! using Legendre's Formula
    primes = []
    is_prime = [True] * (n + 1)
    for p in range(2, n + 1):
        if is_prime[p]:
            primes.append(p)
            for i in range(p * p, n + 1, p):
                is_prime[i] = False

    divisors_count = 1
    for p in primes:
        exponent = 0
        power_of_p = p
        while power_of_p <= n:
            exponent += n // power_of_p
            power_of_p *= p
        divisors_count *= (exponent + 1)

    return divisors_count

print(count_divisors_factorial(50))
