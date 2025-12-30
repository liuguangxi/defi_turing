import math

def get_primes(n):
    """Sieve of Eratosthenes to generate a list of prime numbers."""
    primes = []
    is_prime = [True] * (n + 1)
    for p in range(2, n + 1):
        if is_prime[p]:
            primes.append(p)
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
    return primes

def solve():
    # Number of peaks in the mountain range
    num_peaks = 10000

    # We need 2 * 10000 primes for the left and right heights of each mountain.
    # The 20,000th prime is around 224,737. 300,000 is a safe upper bound for the sieve.
    primes = get_primes(300000)

    # Peak coordinates (x_k, y_k)
    # The terrain consists of mountains with 45-degree slopes.
    # For mountain k, left height is p_{2k-1}, right height is p_{2k}.
    # Peak k is reached from the previous valley by going up at 45 degrees.
    # The valley k is reached from peak k by going down at 45 degrees.
    x = [0] * (num_peaks + 1)
    y = [0] * (num_peaks + 1)
    curr_x, curr_y = 0, 0

    for k in range(1, num_peaks + 1):
        p_left = primes[2 * k - 2]
        p_right = primes[2 * k - 1]

        # Ascent: move horizontally and vertically by p_left
        pk_x = curr_x + p_left
        pk_y = curr_y + p_left
        x[k], y[k] = pk_x, pk_y

        # Descent: move horizontally by p_right and vertically by -p_right
        curr_x = pk_x + p_right
        curr_y = pk_y - p_right

    total_visible = 0

    # Calculate visible peaks P(k) for each k from 1 to 10000.
    for k in range(1, num_peaks + 1):
        if k <= 1:
            continue

        count = 0
        # For the current peak P_k, look back at peaks P_j (j < k).
        # A peak P_j is visible if the slope of P_j-P_k is strictly less than
        # the slopes of all P_i-P_k for j < i < k.
        xk, yk = x[k], y[k]
        min_dy, min_dx = 0, 0  # To store the current minimum slope (dy/dx)

        for j in range(k - 1, 0, -1):
            dy = yk - y[j]
            dx = xk - x[j]

            # Condition: current slope < minimum slope seen so far
            # dy/dx < min_dy/min_dx  <=>  dy * min_dx < min_dy * dx
            if count == 0 or dy * min_dx < min_dy * dx:
                count += 1
                min_dy, min_dx = dy, dx

        total_visible += count

    print(total_visible)

solve()
