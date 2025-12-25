def count_april_easter(start, end):
    count = 0
    for y in range(start, end + 1):
        # Meeus/Jones/Butcher algorithm
        a = y % 19
        b = y // 100
        c = y % 100
        d = b // 4
        e = b % 4
        f = (b + 8) // 25
        g = (b - f + 1) // 3
        h = (19 * a + b - d - g + 15) % 30
        i = c // 4
        k = c % 4
        L = (32 + 2 * e + 2 * i - h - k) % 7
        m = (a + 11 * h + 22 * L) // 451
        month = (h + L - 7 * m + 114) // 31

        if month == 4:
            count += 1
    return count

print(count_april_easter(2001, 9999))
