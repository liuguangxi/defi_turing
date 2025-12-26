limit = 10**9
count = 0
n = 1
while True:
    # The average of squares of integers from 1 to n is X = (n+1)(2n+1)/6
    numerator = (n + 1) * (2 * n + 1)
    if numerator % 6 == 0:
        x = numerator // 6
        if x >= limit:
            break
        count += 1
    n += 1
print(count)
