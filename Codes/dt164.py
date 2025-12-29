total_sum = 0
# We iterate through all multiples of 9 less than 10,000,000
for n in range(9, 10000000, 9):
    s = str(n)
    # Check if the number contains at least one zero
    if '0' in s:
        # Remove all zeros from the string representation
        removed_zeros = s.replace('0', '')
        # Check if the remaining number equals n/9
        # This is equivalent to checking if 9 * f(n) == n
        if int(removed_zeros) * 9 == n:
            total_sum += n

print(total_sum)
