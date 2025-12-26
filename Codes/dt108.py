def is_palindromic_in_base(n, b):
    # Get digits of n in base b (little-endian: d0, d1, ..., dk)
    digits = []
    temp = n
    while temp > 0:
        digits.append(temp % b)
        temp //= b

    # "Adding zeros to the left" to make it a palindrome is possible if and only if
    # the core of the number (after removing trailing zeros) is a palindrome.
    # In our little-endian list 'digits', trailing zeros are at the beginning.
    i = 0
    while i < len(digits) and digits[i] == 0:
        i += 1
    core = digits[i:]

    return core == core[::-1]

def solve():
    count = 0
    # Years in the 3rd millennium: 2001 to 3000 inclusive
    for year in range(2001, 3001):
        # Check bases from 2 to 16 inclusive
        for base in range(2, 17):
            if is_palindromic_in_base(year, base):
                count += 1
                break
    return count

print(solve())
