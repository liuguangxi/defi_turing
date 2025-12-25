def solve():
    limit = 10000
    # Array to store count of solutions for each perimeter p
    # Since p must be even, we only need to look at even indices.
    counts = [0] * (limit + 1)

    # Iterate through each possible perimeter p
    # Note: For p = a + b + c, with a^2 + b^2 = c^2, p must be even.
    for p in range(2, limit, 2):
        # From b = p(p - 2a) / 2(p - a),
        # a < p / (2 + sqrt(2)) approx p/3.414 to ensure a < b < c
        for a in range(1, p // 3):
            # Check if b = p(p-2a) / 2(p-a) is an integer
            num = p * (p - 2 * a)
            den = 2 * (p - a)
            if num % den == 0:
                counts[p] += 1

    # Find the p with the maximum count
    max_count = 0
    best_p = 0
    for p in range(limit):
        if counts[p] > max_count:
            max_count = counts[p]
            best_p = p

    return best_p

print(solve())
