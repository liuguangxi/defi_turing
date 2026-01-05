import math

def get_x(a_set, primes):
    """Calculates the smallest x given a set of exponents 2*a_i."""
    a_sorted = sorted(a_set, reverse=True)
    res = 1
    for i, a in enumerate(a_sorted):
        res *= pow(primes[i], 2 * a)
    return res

def solve():
    """
    Finds F(n) for n = 1, 3, ..., 21 and returns the sum.
    F(n) is the smallest x such that D(x^2)/D(x) = n.
    If x = product of primes p_i^e_i, then D(x^2)/D(x) = product of (2e_i+1)/(e_i+1) = n.
    For this to be an integer, each e_i must be even (e_i = 2a_i).
    The search explores combinations of a_i that satisfy product (4a_i+1)/(2a_i+1) = n.
    """
    targets = {n for n in range(1, 23) if n % 2 != 0}
    best_x = {n: float('inf') for n in targets}
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

    def search(k, last_a, cur_num, cur_den, current_a_set):
        # Check if current ratio is an integer and in our target set
        if cur_num % cur_den == 0:
            n_val = cur_num // cur_den
            if n_val in targets:
                x_val = get_x(current_a_set, primes)
                if x_val < best_x[n_val]:
                    best_x[n_val] = x_val

        # Max factors k=10 is safe as (4a+1)/(2a+1) >= 1.66
        if k >= 10:
            return

        for a in range(last_a, 0, -1):
            # Ratio for this a is (4*a + 1) / (2*a + 1)
            new_num = cur_num * (4 * a + 1)
            new_den = cur_den * (2 * a + 1)

            # Pruning: ratios are always > 1, so if current product exceeds 21, it won't return to target range
            if new_num > 21 * new_den:
                continue

            common = math.gcd(new_num, new_den)
            current_a_set.append(a)
            search(k + 1, a, new_num // common, new_den // common, current_a_set)
            current_a_set.pop()

    # Base case: F(1) = 1 (no prime factors)
    best_x[1] = 1

    # Run the search for combinations of a_i in range [1, 70]
    search(0, 70, 1, 1, [])

    # Calculate the sum of all found F(n) values
    print(best_x)
    total_sum = sum(best_x[n] for n in targets if best_x[n] != float('inf'))

    # Return the 12 rightmost digits
    return total_sum % 10**12

print(solve())
