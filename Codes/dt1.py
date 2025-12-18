def sum_multiples(k, limit):
    """Calculates the sum of multiples of k less than limit."""
    n = (limit - 1) // k
    return k * n * (n + 1) // 2

limit = 2013

# Inclusion-Exclusion Principle
result = (sum_multiples(5, limit) + sum_multiples(7, limit) - sum_multiples(35, limit))
print(result)
