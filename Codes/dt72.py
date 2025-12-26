def solve():
    count = 0
    limit = 31623
    for k in range(limit):
        n = k * k
        last_three = n % 1000
        d = last_three % 10
        if last_three == 111 * d:
            # Check fourth digit
            fourth_digit = (n // 1000) % 10
            if fourth_digit != d:
                count += 1
    return count

print(solve())
