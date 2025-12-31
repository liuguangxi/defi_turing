def solve():
    """
    Finds the number of lucky numbers in the range [1, 100,000] using the
    sieve procedure described by Stanislaw Ulam.
    """
    limit = 100000

    # Step 1: Remove even numbers.
    # We start with all odd numbers up to the limit.
    nums = list(range(1, limit + 1, 2))

    # lucky_idx will track the position of the next lucky number to use for sieving.
    # Initial list is [1, 3, 5, 7, ...].
    # Index 0 is '1' (already lucky), index 1 is '3' (the first sifter).
    lucky_idx = 1

    while lucky_idx < len(nums):
        # L is the value of the current lucky number indicating the rank to remove.
        L = nums[lucky_idx]

        # If the rank to remove is greater than the current list length, we stop.
        if L > len(nums):
            break

        # Remove every L-th element.
        # The L-th element in 1-based ranking is at index L-1 in 0-based indexing.
        # Python slice deletion 'del lst[start::step]' is highly efficient.
        del nums[L-1::L]

        # Move to the next lucky number in the updated list.
        lucky_idx += 1

    return len(nums)

print(solve())
