def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

def solve():
    # A 7-digit palindrome is formed by its first 4 digits: d1 d2 d3 d4 d3 d2 d1
    # We iterate from 9999 down to 1000 to find the largest one.
    for i in range(9999, 999, -1):
        s = str(i)
        # Construct the palindrome: s[0]s[1]s[2]s[3]s[2]s[1]s[0]
        p_str = s + s[-2::-1]
        p = int(p_str)

        # Check if the square is also a palindrome
        if is_palindrome(p * p):
            return p

print(solve())
