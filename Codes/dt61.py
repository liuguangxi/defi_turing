def has_no_isolated_digits(n):
    s = str(n)
    if len(s) == 1: return False
    if s[0] != s[1]: return False
    if s[-1] != s[-2]: return False
    for i in range(1, len(s) - 1):
        if s[i] != s[i-1] and s[i] != s[i+1]:
            return False
    return True

def solve():
    count = 0
    n = 1
    while True:
        if n % 10 != 0:
            if has_no_isolated_digits(n * n):
                count += 1
                if count == 4:
                    return n
        n += 1

print(solve())
