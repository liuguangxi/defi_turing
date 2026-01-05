import itertools

def count_partitions(target_sum, nums, group_size, num_groups):
    """
    Counts the number of ways to partition the set 'nums' into 'num_groups'
    disjoint subsets, each of size 'group_size' and summing to 'target_sum'.
    The order of the subsets in the partition does not matter.
    """
    if num_groups == 0:
        return 1

    # Sort numbers and take the smallest to ensure each partition is counted once
    nums_list = sorted(list(nums))
    first = nums_list[0]
    rest = nums_list[1:]

    # Pruning: check if target is achievable with smallest/largest remaining numbers
    if first + sum(nums_list[-(group_size-1):]) < target_sum:
        return 0
    if first + sum(nums_list[1:group_size]) > target_sum:
        return 0

    cnt = 0
    # Every valid partition must have the 'first' element in exactly one group.
    # We find all possible groups that contain this element.
    for combo in itertools.combinations(rest, group_size - 1):
        if sum(combo) + first == target_sum:
            cnt += count_partitions(target_sum, nums - set(combo) - {first}, group_size, num_groups - 1)
    return cnt

def solve():
    # n polygons with n sides meeting at a common vertex.
    # Total vertices V = n * (n - 1) + 1.
    n = 5
    V = n * (n - 1) + 1  # For n=5, V=21
    total_sum = V * (V + 1) // 2

    # S = ( (n-1)*x + sum(1..V) ) / n must be the integer sum of each polygon's vertices.
    # The sum of the (n-1) vertices excluding the center for each polygon is target_sum = S - x.
    total_partitions = 0
    for x in range(1, V + 1):
        if ((n - 1) * x + total_sum) % n == 0:
            S = ((n - 1) * x + total_sum) // n
            target_sum_per_group = S - x
            nums_to_partition = set(range(1, V + 1)) - {x}
            # Each partition is a set of n groups of size (n-1).
            p = count_partitions(target_sum_per_group, nums_to_partition, n - 1, n)
            total_partitions += p

    # Each partition defines:
    # 1. An assignment of the n groups to the n polygons (n! ways)
    # 2. For each polygon, an assignment of the (n-1) numbers to the (n-1) distinct vertex positions ((n-1)! ways per polygon)
    # Total ways = total_partitions * n! * ((n-1)!)^n
    factor = 1 # Using math.factorial effectively
    import math
    ways_per_partition = math.factorial(n) * (math.factorial(n - 1) ** n)

    result = total_partitions * ways_per_partition
    return result

print(solve())
