def contains_origin(x1, y1, x2, y2, x3, y3):
    # Check if the origin (0,0) is inside the triangle using cross products.
    # The origin is inside if it lies on the same side of all three edges.
    cp1 = x1 * y2 - x2 * y1
    cp2 = x2 * y3 - x3 * y2
    cp3 = x3 * y1 - x1 * y3
    return (cp1 > 0 and cp2 > 0 and cp3 > 0) or (cp1 < 0 and cp2 < 0 and cp3 < 0)

def solve():
    count = 0
    with open('120-fichier.txt', 'r') as f:
        for line in f:
            # Handle various delimiters like commas or spaces
            coords = list(map(int, line.replace(',', ' ').split()))
            if len(coords) == 6:
                if contains_origin(*coords):
                    count += 1
    return count

print(solve())
