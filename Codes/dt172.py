def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

limit = 1000000
total_sum = 0

# A pair (n, n+1) where both n and n+1 are less than 1,000,000.
# The problem asks for the sum of the smallest integers (n) in these pairs.
for n in range(limit - 1):
    if sum_digits(n) % 7 == 0 and sum_digits(n + 1) % 7 == 0:
        total_sum += n

print(total_sum)
