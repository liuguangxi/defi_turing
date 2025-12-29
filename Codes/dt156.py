import math

def solve():
    # Search for the smallest n such that 18^n ends with the digits of n.
    # Let k be the number of digits in n. The condition is 18^n % 10^k == n.
    for n in range(1, 1000):
        k = len(str(n))
        mod = 10**k
        if pow(18, n, mod) == n:
            return n

print(solve())
