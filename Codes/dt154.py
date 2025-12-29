import math

def is_power_of_10(n):
    """Checks if n is a power of 10 (10, 100, 1000, ...)."""
    if n <= 0: return False
    s = str(n)
    return s[0] == '1' and all(c == '0' for c in s[1:])

def solve():
    """
    Finds the smallest integer n > 1 that is not a power of 10 and
    such that the set of digits of n^3 is the same as the set of digits of n.
    """
    n = 2
    while True:
        if not is_power_of_10(n):
            s_n = set(str(n))
            s_n3 = set(str(n**3))

            # The problem asks for n^3 to be written using the 'same digits' as n.
            # In mathematical puzzles, this typically means the sets of digits are identical.
            if s_n3 == s_n:
                return n
        n += 1

print(solve())
