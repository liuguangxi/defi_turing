import itertools

def solve():
    """
    Finds positive integers less than one billion where the i-th digit (d_i)
    represents the count of the digit 'i' in the number itself.
    These are known as self-descriptive numbers.
    For a number of length L, we search for digits d_0, d_1, ..., d_L-1
    such that d_i is the count of the digit 'i' in the sequence.
    This implies:
    1. sum(d_i) = L (total number of positions)
    2. sum(i * d_i) = L (total sum of the digits, which must equal the count
       of digits present in the positions)
    """
    solutions = []
    # Search for all possible lengths L from 1 to 9 (as numbers must be < 10^9)
    for L in range(1, 10):
        # We search for sequences (d_0, ..., d_L-1) satisfying the constraints
        def search(idx, current_sum, weighted_sum):
            if idx == L:
                if current_sum == L and weighted_sum == L:
                    return [[]]
                return []

            res = []
            # Optimization based on the two sum constraints
            for di in range(L + 1):
                if current_sum + di > L:
                    break
                if weighted_sum + idx * di > L:
                    break

                tails = search(idx + 1, current_sum + di, weighted_sum + idx * di)
                for t in tails:
                    res.append([di] + t)
            return res

        candidates = search(0, 0, 0)
        for p in candidates:
            # The first digit cannot be zero
            if p[0] == 0:
                continue

            # Check consistency: verify that p[i] correctly counts digit i in sequence p
            counts = [0] * L
            valid = True
            for digit in p:
                if digit < L:
                    counts[digit] += 1
                else:
                    # If any digit in the number is >= L, it cannot be described
                    # by the positions 0...L-1, making the description incomplete.
                    valid = False
                    break

            if valid and all(counts[i] == p[i] for i in range(L)):
                # Convert the sequence of digits to an integer
                num_str = "".join(map(str, p))
                solutions.append(int(num_str))

    # Return the sum of all distinct numbers found
    return sum(set(solutions))

print(solve())
