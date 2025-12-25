def solve():
    limit = 2013

    # 1. Calculate the sum of proper divisors for all n up to limit
    div_sum = [0] * (limit + 1)
    for i in range(1, limit // 2 + 1):
        for j in range(2 * i, limit + 1, i):
            div_sum[j] += i

    # 2. Identify abundant numbers
    abundants = [i for i in range(1, limit + 1) if div_sum[i] > i]

    # 3. Mark all numbers that are the sum of two abundant numbers
    is_sum_of_two = [False] * (limit + 1)
    for i in range(len(abundants)):
        for j in range(i, len(abundants)):
            s = abundants[i] + abundants[j]
            if s <= limit:
                is_sum_of_two[s] = True
            else:
                # Since abundants is sorted, we can break inner loop early
                break

    # 4. Sum integers that were never marked
    result = sum(i for i in range(1, limit + 1) if not is_sum_of_two[i])
    return result

print(solve())
