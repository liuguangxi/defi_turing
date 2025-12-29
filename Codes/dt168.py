def check_digits(n):
    s = str(n)
    even = {'0', '2', '4', '6', '8'}
    odd = {'1', '3', '5', '7', '9'}
    chars = set(s)
    return chars.issubset(even) or chars.issubset(odd)

total_sum = 0
for x in range(1, 1000):
    square = x * x
    if check_digits(square):
        total_sum += square

print(total_sum)
