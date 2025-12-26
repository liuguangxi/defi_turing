from collections import Counter

def solve():
    # counts dictionary to store how many times each number appears in Pascal's triangle
    counts = Counter()

    # We search for the smallest number greater than 1 appearing 8 times.
    # We set an initial search limit based on the known candidate 3003.
    limit = 3003

    # Iterate through row n of Pascal's triangle
    # n-th row has n+1 entries: C(n, 0), C(n, 1), ..., C(n, n)
    for n in range(1, limit + 1):
        # We only need to compute k up to n/2 because C(n, k) = C(n, n-k)
        for k in range(1, n // 2 + 1):
            val = 1
            is_within_limit = True
            # Compute binomial coefficient C(n, k) iteratively
            for i in range(k):
                val = val * (n - i) // (i + 1)
                if val > limit:
                    is_within_limit = False
                    break

            # If C(n, k) exceeds the limit, stop checking larger k in this row
            if not is_within_limit:
                break

            # Count the occurrences (2 if symmetric, 1 if middle element)
            if 2 * k == n:
                counts[val] += 1
            else:
                counts[val] += 2

    # Filter numbers greater than 1 that appear at least 8 times
    candidates = [val for val, count in counts.items() if val > 1 and count >= 8]
    return min(candidates) if candidates else None

print(solve())
