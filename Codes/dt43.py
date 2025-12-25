def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

def solve():
    limit = int((10**13 - 1)**0.5)
    return sum(x for x in range(1, limit + 1) if is_palindrome(x * x))

print(solve())
