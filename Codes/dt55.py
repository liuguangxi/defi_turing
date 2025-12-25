def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

def is_lychrel(n):
    for _ in range(50):
        n += int(str(n)[::-1])
        if is_palindrome(n):
            return False
    return True

def solve():
    return sum(1 for i in range(1, 10000) if is_lychrel(i))

print(solve())
