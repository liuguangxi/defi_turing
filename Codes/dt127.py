import datetime

def solve():
    # Set to store found calendar types: (weekday, is_leap)
    seen_calendars = set()
    years_sum = 0
    year = 2016

    while len(seen_calendars) < 14:
        # Determine if the year is a leap year
        is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        # Determine the weekday of Jan 1st (0 is Monday, 6 is Sunday)
        weekday = datetime.date(year, 1, 1).weekday()

        calendar_type = (weekday, is_leap)

        if calendar_type not in seen_calendars:
            seen_calendars.add(calendar_type)
            years_sum += year

        year += 1

    return years_sum

print(solve())
