def is_prime(n):
    if n < 2: return False
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n % 3 == 0: return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0: return False
        i += 6
    return True

def check_property(s):
    n = len(s)
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            if not is_prime(int(s[i:i+length])):
                return False
    return True

def solve():
    # Only digits that can form 2-digit primes are considered.
    # Digits at indices > 0 must be 1, 3, 7, 9 to ensure 2-digit substrings are prime.
    max_prime = 0
    stack = [(str(d), d) for d in range(1, 10)]

    while stack:
        s, val = stack.pop()

        # Check substrings if length >= 2
        if len(s) >= 2:
            if not check_property(s):
                continue
            max_prime = max(max_prime, val)

        if len(s) < 7:
            for d in [1, 3, 7, 9]:
                new_s = s + str(d)
                new_val = int(new_s)
                if new_val < 10000000:
                    stack.append((new_s, new_val))

    return max_prime

print(solve())
