def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

def solve():
    # Let the three consecutive strictly positive even integers be 2n, 2n+2, 2n+4.
    # We iterate through n starting from 1 to find the smallest product that is a palindrome.
    n = 1
    while True:
        a = 2 * n
        b = a + 2
        c = b + 2
        product = a * b * c
        if is_palindrome(product):
            return product
        n += 1

print(solve())
