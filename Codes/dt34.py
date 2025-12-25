import math

def solve():
    # Precompute factorials for digits 0-9
    fact = [math.factorial(i) for i in range(10)]

    results = []
    # Upper bound calculated as 7 * 9!
    for n in range(10, 2540161):
        # Calculate sum of factorials of digits
        digit_sum = sum(fact[int(d)] for d in str(n))

        if digit_sum == n:
            results.append(n)

    # Calculate the product of the found numbers
    product = 1
    for val in results:
        product *= val
    return product

print(solve())
