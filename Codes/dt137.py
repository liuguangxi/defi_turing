from fractions import Fraction

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solve():
    # Sisyphus moves on squares 0-105.
    # Primes less than 100 are the "losing" squares.
    primes_less_than_100 = {x for x in range(100) if is_prime(x)}

    # p[i] will store the probability of winning starting from square i.
    # We use Fraction to maintain precision and find the irreducible numerator.
    p = [Fraction(0)] * 106

    # Square numbers 100 and above are winning states.
    for i in range(100, 106):
        p[i] = Fraction(1)

    # We iterate backwards from square 99 down to 0.
    for i in range(99, -1, -1):
        if i in primes_less_than_100:
            # Sisyphus loses if he lands on a prime square < 100.
            p[i] = Fraction(0)
        else:
            # If he is on a safe square, he rolls a six-sided die (1-6).
            # The win probability is the average of the win probabilities of the next 6 squares.
            p[i] = sum(p[i+1 : i+7]) / 6

    # The starting win probability is stored in p[0].
    win_prob = p[0]

    # Return the last ten digits of the numerator of the irreducible fraction.
    return win_prob.numerator % 10**10

print(solve())
