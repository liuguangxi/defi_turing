def solve_keith_numbers():
    total_result = 0
    # Iterate through all numbers between 10 and 1,000,000.
    for k in range(10, 1000001):
        # Extract digits of the number k.
        digits = [int(x) for x in str(k)]
        n = len(digits)
        # Initialize the Fibonacci-like sequence with the digits of k.
        # The first term after the digits is the sum of those digits.
        seq = digits + [sum(digits)]
        i = n

        # Use the recurrence a_{i+1} = 2*a_i - a_{i-n} to generate the next terms.
        # This is equivalent to summing the last n terms of the sequence.
        while seq[i] < k:
            seq.append(2 * seq[i] - seq[i - n])
            i += 1

        # If the number k appears in the generated sequence, it is a Keith number.
        if seq[i] == k:
            # The length of the sequence is the number of terms generated (index i + 1).
            total_result += k * (i + 1)

    # Output the calculated sum.
    print(total_result)

solve_keith_numbers()
