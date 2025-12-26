import datetime

def solve():
    count = 0
    # Iterate through all years from 2001 to 2100 inclusive
    for year in range(2001, 2101):
        # Iterate through all months
        for month in range(1, 13):
            # Check if the 13th day is a Friday (weekday() returns 4 for Friday)
            if datetime.date(year, month, 13).weekday() == 4:
                count += 1
    return count

print(solve())
