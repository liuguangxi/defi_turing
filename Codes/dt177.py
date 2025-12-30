def count_zeros(n):
    count = 0
    while n >= 5:
        n //= 5
        count += n
    return count

print(count_zeros(100_000_000))
