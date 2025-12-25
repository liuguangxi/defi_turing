def solve():
    # Precompute 5th powers for efficiency
    powers = [i**5 for i in range(10)]

    total_sum = 0
    # Search from 2 to the calculated upper bound
    # 1 is excluded as per the problem description
    for n in range(2, 355000):
        # Calculate sum of 5th powers of digits
        digit_sum = sum(powers[int(d)] for d in str(n))

        if digit_sum == n:
            total_sum += n

    return total_sum

print(solve())
