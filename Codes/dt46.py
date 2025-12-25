def is_prime(n):
    if n < 2: return False
    if n % 2 == 0: return n == 2
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def solve():
    n = 9
    while True:
        if not is_prime(n):
            found = False
            k = 1
            while 2 * k * k < n:
                if is_prime(n - 2 * k * k):
                    found = True
                    break
                k += 1
            if not found:
                return n
        n += 2

print(solve())
