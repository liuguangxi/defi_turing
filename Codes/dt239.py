from collections import Counter

def get_exponents(n):
    primes = []
    is_prime = [True] * (n + 1)
    for p in range(2, n + 1):
        if is_prime[p]:
            primes.append(p)
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
    exponents = []
    for p in primes:
        count = 0
        m = n
        while m >= p:
            count += m // p
            m //= p
        exponents.append(count)
    return primes, exponents

primes_list, exponents = get_exponents(40)
# Factorizations for all numbers k in [1, max(exponents)+1]
max_val = max(exponents) + 2
factorizations = []
for k in range(max_val + 1):
    f = [0] * len(primes_list)
    temp = k
    if k > 0:
        for i, p in enumerate(primes_list):
            while temp % p == 0:
                f[i] += 1
                temp //= p
    factorizations.append(tuple(f))

dp = {(0,) * len(primes_list): 1}
for e in exponents:
    new_dp = Counter()
    # k = x_i + 1, where 0 <= x_i <= e_i, so 1 <= k <= e_i + 1
    for k in range(1, e + 2):
        f_num = factorizations[k]
        f_den = factorizations[e - k + 2]
        # Calculate the prime exponent differences for the ratio (x_i + 1) / (e_i - x_i + 1)
        diff = tuple(f_num[i] - f_den[i] for i in range(len(primes_list)))
        for ratio, count in dp.items():
            new_ratio = tuple(ratio[i] + diff[i] for i in range(len(primes_list)))
            new_dp[new_ratio] += count
    dp = new_dp

# The answer is the number of solutions where the product of ratios is 1 (all prime exponents are zero).
# Since 40! is not a perfect square, a cannot equal b, so we divide the total count by 2.
total_solutions = dp[(0,) * len(primes_list)]
print(total_solutions // 2)
