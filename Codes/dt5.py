# Calculate 2 raised to the power of 2222
power_value = 2**2222

# Convert the number to a string and sum the integer value of each character
digit_sum = sum(int(digit) for digit in str(power_value))
print(digit_sum)
