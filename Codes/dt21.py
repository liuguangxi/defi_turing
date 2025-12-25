def solve():
    # Find all years from 1 to 2013 with distinct digits
    distinct_years = []
    for year in range(1, 2014):
        s = str(year)
        if len(set(s)) == len(s):
            distinct_years.append(year)

    # a) Total number of such years
    count_a = len(distinct_years)

    # b) Longest period between two consecutive dates
    max_period_b = 0
    for i in range(1, len(distinct_years)):
        period = distinct_years[i] - distinct_years[i-1]
        if period > max_period_b:
            max_period_b = period

    return count_a, max_period_b, count_a * max_period_b

a, b, result = solve()
print(f"Number of years: {a}")
print(f"Longest period: {b}")
print(result)
