def sum_digits(n):
    return sum(int(d) for d in str(n))

max_n = 0
# We search up to 100 because the sum of digits of n^3 grows logarithmically,
# while n grows linearly. For n >= 100, n^3 has at most 9 digits (if n < 1000),
# so the max sum of digits is 9 * 9 = 81, which is already less than n.
for n in range(1, 100):
    if n == sum_digits(n**3):
        max_n = n

print(max_n)
