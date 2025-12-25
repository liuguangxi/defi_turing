def is_prime(n):
    if n < 2: return False
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n % 3 == 0: return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_left_truncatable(n):
    s = str(n)
    for i in range(1, len(s)):
        if not is_prime(int(s[i:])):
            return False
    return True

def solve():
    # Start with single-digit primes (seeds for RTP)
    rtp_candidates = [2, 3, 5, 7]
    truncatable_primes = []

    i = 0
    while i < len(rtp_candidates):
        base = rtp_candidates[i]
        # Try appending digits to the right
        for digit in [1, 3, 7, 9]:
            new_val = base * 10 + digit
            if is_prime(new_val):
                rtp_candidates.append(new_val)
                # If it's also left-truncatable, it's a solution
                if is_left_truncatable(new_val):
                    truncatable_primes.append(new_val)
        i += 1

    return sum(truncatable_primes)

print(solve())
