def solve():
    max_sum = 0
    for a in range(1, 250):
        for b in range(1, 250):
            digit_sum = sum(int(d) for d in str(a**b))
            if digit_sum > max_sum:
                max_sum = digit_sum
    return max_sum

print(solve())
