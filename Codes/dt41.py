import itertools

def is_prime(n):
    if n < 2: return False
    if n % 2 == 0: return n == 2
    if n % 3 == 0: return n == 3
    for i in range(5, int(n**0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def solve():
    # A pandigital number of n digits is divisible by 3 if the sum 1..n is divisible by 3.
    # n=9: sum=45 (divisible by 9)
    # n=8: sum=36 (divisible by 9)
    # n=7: sum=28 (not divisible by 3) - Largest potential candidate

    digits = "7654321"
    for p in itertools.permutations(digits):
        num = int("".join(p))
        if is_prime(num):
            return num
    return None

print(solve())
