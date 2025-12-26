from itertools import combinations_with_replacement

def solve():
    # Precompute the 7th powers of digits 0-9
    powers = [i**7 for i in range(10)]
    results = []

    # Iterate through all combinations of 7 digits with replacement
    # There are only 11,440 such combinations.
    for combo in combinations_with_replacement(range(10), 7):
        # Calculate the sum of the 7th powers of these digits
        s = sum(powers[d] for d in combo)

        # Check if the sum is exactly a 7-digit number
        if 1_000_000 <= s <= 9_999_999:
            # Extract digits of s and check if they match the combination
            s_digits = sorted([int(d) for d in str(s)])
            if s_digits == sorted(list(combo)):
                results.append(s)

    # Return the sum of unique numbers found
    return sum(set(results))

# Execution
total_sum = solve()
print(total_sum)
