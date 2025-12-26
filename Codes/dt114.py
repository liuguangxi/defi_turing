def find_kaprekar_number(target_index):
    count = 0
    k = 1
    while True:
        # Number of digits n in k
        n = len(str(k))
        # Split k^2 into right part R with n digits and left part L
        l, r = divmod(k * k, 10**n)

        # Kaprekar condition: sum of parts equals the number itself
        if l + r == k:
            count += 1
            if count == target_index:
                return k
        k += 1

print(find_kaprekar_number(49))
