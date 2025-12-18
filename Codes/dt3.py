def largest_prime_factor(n):
    d = 2
    while d * d <= n:
        while n % d == 0:
            n //= d
        d += 1
    return n

result = largest_prime_factor(20130101)
print(result)
