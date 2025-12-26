def sum_of_divisors(limit):
    sigma = [0] * limit
    for i in range(1, limit):
        for j in range(i, limit, i):
            sigma[j] += i
    return sigma

def solve():
    limit = 100000
    sigma_values = sum_of_divisors(limit)

    # Subtriple: sum of proper divisors s(n) = 3n
    # Total sum of divisors sigma(n) = s(n) + n = 4n
    subtriples = [n for n in range(1, limit) if sigma_values[n] == 4 * n]

    return sum(subtriples)

print(solve())
