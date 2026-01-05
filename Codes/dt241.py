import itertools

def solve():
    """
    To find the counterfeit bags (11g and 12g) in one weighing, we take x_i coins from bag i.
    Let i be the bag with 11g coins and j be the bag with 12g coins.
    The total mass W(i, j) is:
    W(i, j) = 11*x_i + 12*x_j + 10*(S - x_i - x_j) = 10*S + x_i + 2*x_j
    where S = sum(x_k) for k=1 to 8.

    For the weighing to be unique for each of the 56 permutations of (i, j),
    the 56 values of x_i + 2*x_j must be distinct.
    To minimize the total number of coins S, we look for a set of 8 distinct
    non-negative integers {x_1, ..., x_8} that satisfies this uniqueness
    condition and minimizes the sum S.
    """

    def is_valid(x_list):
        """Checks if all permutations x_i + 2*x_j are distinct."""
        sums = set()
        n = len(x_list)
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                val = x_list[i] + 2 * x_list[j]
                if val in sums:
                    return False
                sums.add(val)
        return True

    best_S = float('inf')
    best_x = []

    def find_minimal_set(current_set, current_sum, last_val):
        nonlocal best_S, best_x
        # If we have 8 elements, we found a candidate set
        if len(current_set) == 8:
            if current_sum < best_S:
                best_S = current_sum
                best_x = current_set[:]
            return

        # Pruning based on best sum found so far
        rem = 8 - len(current_set)
        if current_sum + rem * (last_val + 1) + rem * (rem - 1) // 2 >= best_S:
            return

        # Explore possible next values
        for val in range(last_val + 1, 32):  # Sufficiently large range for search
            temp_set = current_set + [val]
            if is_valid(temp_set):
                find_minimal_set(temp_set, current_sum + val, val)

    # Start search from non-negative integers
    find_minimal_set([], 0, -1)

    # The sum of all 56 distinct masses:
    # Sum_{i != j} (10*S + x_i + 2*x_j)
    # = 560*S + Sum_{i != j} x_i + Sum_{i != j} 2*x_j
    # Across all 56 pairs, each x_k appears 7 times as the 11g coin bag (x_i)
    # and 7 times as the 12g coin bag (x_j).
    # Total = 560*S + 7*S + 14*S = 581*S

    return 581 * best_S

print(solve())
