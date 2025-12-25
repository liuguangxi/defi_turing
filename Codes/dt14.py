def solve():
    cache = {1: 1}
    max_len = 0
    best_numbers = []

    for i in range(1, 1500000):
        curr = i
        stack = []
        # Calculate sequence until we hit a known value
        while curr not in cache:
            stack.append(curr)
            if curr % 2 == 0:
                curr //= 2
            else:
                curr = 3 * curr + 1

        # Backfill cache with lengths
        current_length = cache[curr]
        while stack:
            node = stack.pop()
            current_length += 1
            cache[node] = current_length

        # Update results
        if current_length > max_len:
            max_len = current_length
            best_numbers = [i]
        elif current_length == max_len:
            best_numbers.append(i)

    return min(best_numbers)

print(solve())
