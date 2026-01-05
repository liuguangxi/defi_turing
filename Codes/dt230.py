from fractions import Fraction
import math

def solve():
    """
    S(n) is the expected number of shuffles to sort n cards.
    Stapled groups are blocks of consecutive numbers (e.g., 1-2-3).
    When k such blocks are shuffled, the number of blocks in the next state
    depends on how many adjacencies of the form (i, i+1) are created.
    """

    # D[m] is the number of permutations of {1, ..., m} with no adjacencies (i, i+1).
    # Inclusion-Exclusion formula for successions:
    def get_D(m):
        return sum((-1)**j * math.comb(m-1, j) * math.factorial(m-j) for j in range(m))

    D = [0] * 12
    for m in range(1, 12):
        D[m] = get_D(m)

    # P(m, a) is the number of permutations of m elements with exactly 'a' adjacencies.
    def P(m, a):
        return math.comb(m-1, a) * D[m-a]

    # E[k] is the expected number of tosses to reach the sorted state starting
    # from a state with k blocks.
    E = [Fraction(0)] * 11
    for k in range(2, 11):
        # E[k] = 1 + sum_{a=0}^{k-1} Prob(a adjacencies) * E[k-a]
        # E[k] = 1 + (1/k!) * sum_{a=0}^{k-1} P(k, a) * E[k-a]
        # Rearranging to solve for E[k]:
        num = math.factorial(k) + sum(P(k, a) * E[k-a] for a in range(1, k))
        den = math.factorial(k) - P(k, 0)
        E[k] = Fraction(num, den)

    # S(n) is the initial expected value considering the first check.
    # S(n) = sum_{k=1}^n Prob(initial deck has k blocks) * E[k]
    # (Note: E[1] = 0, so the sorted case contributes 0).
    n = 10
    S10 = Fraction(sum(P(n, a) * E[n-a] for a in range(n)), math.factorial(n))

    # Convert to decimal string and extract the first 11 digits.
    def fraction_to_digits(f, count):
        num = f.numerator
        den = f.denominator
        whole = str(num // den)
        digits = whole
        rem = num % den
        while len(digits) < count:
            rem *= 10
            digits += str(rem // den)
            rem %= den
        return digits[:count]

    return fraction_to_digits(S10, 11)

print(solve())
