def count_divisors(n):
    cnt = 1
    p = 2
    temp = n
    while p * p <= temp:
        if temp % p == 0:
            exponent = 0
            while temp % p == 0:
                exponent += 1
                temp //= p
            cnt *= (exponent + 1)
        p += 1
    if temp > 1:
        cnt *= 2
    return cnt

def solve():
    n = 1
    while True:
        # Use the property: d(n * (n+1) / 2)
        if n % 2 == 0:
            divs = count_divisors(n // 2) * count_divisors(n + 1)
        else:
            divs = count_divisors(n) * count_divisors((n + 1) // 2)

        if divs > 1000:
            return n * (n + 1) // 2
        n += 1

print(solve())
