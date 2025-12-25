def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

def solve():
    # Starting from the root of 698896, which is 836
    # Even-length palindromes are always divisible by 11.
    # Thus, their square roots must also be divisible by 11.
    n = 836 + 11
    while True:
        sq = n * n
        s_sq = str(sq)
        # Check if the square is a palindrome and has an even number of digits
        if len(s_sq) % 2 == 0:
            if s_sq == s_sq[::-1]:
                return sq
        n += 11

print(solve())
