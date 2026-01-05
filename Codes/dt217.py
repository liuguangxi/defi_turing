def is_prime(n):
    """Checks if n is a prime number."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solve():
    """
    Solves the beetle problem.
    Beetles are placed on prime numbers between 0 and 1000.
    Smallest prime is 2, largest prime is 997.
    Beetles at odd-indexed primes move Right, even-indexed move Left.
    Collisions effectively mean beetles pass through each other.
    The time all beetles fall off is the maximum of all individual exit times.
    """
    ruler_length = 1000
    primes = [p for p in range(1, 1001) if is_prime(p)]

    exit_times = []
    for i, p in enumerate(primes):
        # The first beetle (i=0) moves Right, the second (i=1) moves Left, etc.
        # Right-moving beetle at p takes (ruler_length - p) to exit.
        # Left-moving beetle at p takes (p - 0) to exit.
        if (i + 1) % 2 != 0:  # Odd-indexed beetle (1st, 3rd, ...)
            exit_times.append(ruler_length - p)
        else:  # Even-indexed beetle (2nd, 4th, ...)
            exit_times.append(p)

    # The maximum exit time is the time until the last beetle falls off.
    # For the first beetle (p=2) moving Right: 1000 - 2 = 998.
    # For the last beetle (p=997) moving Left: 997 - 0 = 997.
    return max(exit_times)

print(solve())
