def solve():
    count = 0
    # Iterating through numbers from 10 to 10,000,000
    for i in range(10, 10000001):
        n = i
        # The image is the final single-digit result of multiplying digits repeatedly.
        while n > 9:
            # If a number contains 0, the product of its digits is 0.
            if '0' in str(n):
                n = 0
                break
            prod = 1
            temp = n
            while temp:
                prod *= (temp % 10)
                temp //= 10
            n = prod
        # We are looking for numbers whose final image is 6.
        if n == 6:
            count += 1
    return count

print(solve())
