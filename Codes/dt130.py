def solve():
    # The problem asks for the horizontal line y = k that minimizes the sum of distances to
    # a set of points (xi, yi). This sum is Σ |yi - k|.
    # The value k that minimizes this sum is the median of the y-coordinates.
    # If there are an even number of points (N=1000), any value in the interval
    # [y_median_low, y_median_high] is a solution.
    # The average of these heights is (y_median_low + y_median_high) / 2.

    y_coords = []
    with open('130-fichier.txt', 'r') as f:
        for line in f:
            # Handle potential comma or space delimiters
            parts = line.replace(',', ' ').split()
            if len(parts) >= 2:
                y_coords.append(float(parts[1]))
    y_coords.sort()
    n = len(y_coords)
    if n % 2 == 1:
        return y_coords[n // 2]
    else:
        # Average of the two middle values for an even number of points
        return (y_coords[n // 2 - 1] + y_coords[n // 2]) / 2

print(int(solve()))
