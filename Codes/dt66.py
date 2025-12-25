def get_period_length(d):
    k = d
    while k % 2 == 0: k //= 2
    while k % 5 == 0: k //= 5
    if k <= 1: return 0

    # Calculate the multiplicative order of 10 modulo k
    # 10^L ≡ 1 (mod k)
    rem = 1
    for length in range(1, k + 1):
        rem = (rem * 10) % k
        if rem == 1:
            return length
    return 0

def solve():
    max_len = 0
    best_d = 0
    for d in range(1, 5000):
        length = get_period_length(d)
        if length > max_len:
            max_len = length
            best_d = d
    return best_d

print(solve())
