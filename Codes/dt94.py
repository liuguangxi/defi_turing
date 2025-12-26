def solve():
    # Precompute squares of digits
    sq = [i*i for i in range(10)]

    # Precompute whether a sum of squares eventually reaches 89
    # The maximum sum of squares for a 7-digit number up to 5,000,000 is 502 (4^2 + 6*9^2)
    target = [False] * 601
    for i in range(1, 601):
        curr = i
        while curr != 1 and curr != 89:
            s = 0
            temp = curr
            while temp:
                s += sq[temp % 10]
                temp //= 10
            curr = s
        target[i] = (curr == 89)

    # Precompute sum of squares of digits for numbers 000 to 999
    dss3 = [sq[i // 100] + sq[(i // 10) % 10] + sq[i % 10] for i in range(1000)]

    # Frequency of each digit-square sum for 3-digit blocks
    dss3_counts = [0] * 244  # Max sum of squares for 3 digits is 3 * 9^2 = 243
    for s in dss3:
        dss3_counts[s] += 1

    count = 0
    # Iterate through the first 4 digits (0000 to 4999)
    for a in range(5000):
        # Calculate the sum of squares of the first 4 digits
        s_high = dss3[a // 1000] + dss3[a % 1000]
        # Use precomputed frequencies for the last 3 digits
        for s_val, freq in enumerate(dss3_counts):
            if target[s_high + s_val]:
                count += freq

    # The loop above includes n=0. Since target[0] is False, n=0 is not counted.
    # The loop covers 0 to 4,999,999. We check 5,000,000 separately.
    # Sum of squares of digits for 5,000,000 is 5^2 = 25.
    if target[25]:
        count += 1

    return count

print(solve())
