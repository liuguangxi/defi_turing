def solve():
    # S(n) is the sum where '4' digits are alternately replaced by 3 and 5.
    # F(n) is the sum of the first n integers: n*(n+1)/2.
    # We are looking for the largest n < 1,000,000 such that S(n) = F(n).
    # This is equivalent to finding n such that the total difference (S(n) - F(n)) is 0.

    diff = 0
    replace_with = 3
    last_zero = 0
    limit = 1000000

    for i in range(1, limit):
        # Convert number to string to check for the '4' key digit
        s = str(i)
        if '4' in s:
            val_replaced = 0
            # Process each digit to replace '4's alternately with 3 and 5
            for char in s:
                val_replaced *= 10
                if char == '4':
                    val_replaced += replace_with
                    # Toggle between 3 and 5 for the next occurrence of '4'
                    replace_with = 5 if replace_with == 3 else 3
                else:
                    val_replaced += int(char)
            # Add the difference between the modified value and the original i
            diff += (val_replaced - i)

        # Check if the cumulative difference is zero
        if diff == 0:
            last_zero = i

    return last_zero

print(solve())
