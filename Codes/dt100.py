def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

def solve():
    primes = [p for p in range(2, 101) if is_prime(p)]
    # Grid:
    # a  b  7
    # 1  e  f
    # g  13 i
    for e in range(2, 101):
        g, i, a, b, f = 2*e-7, e-6, e+6, 2*e-13, 2*e-1
        if all(x in primes for x in [e, a, b, f, g, i]):
            return a * e * g

print(solve())
