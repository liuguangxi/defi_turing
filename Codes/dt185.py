import heapq

def get_triangle_values(b):
    """Generates all 15 values in the triangle from the bottom row."""
    row = list(b)
    all_vals = []
    all_vals.extend(row)
    for _ in range(4):
        # Calculate the next row by adding adjacent elements
        row = [row[i] + row[i+1] for i in range(len(row)-1)]
        all_vals.extend(row)
    return all_vals

def solve():
    # The total sum S of the 15 numbers can be expressed as a weighted sum
    # of the bottom row elements b1, b2, b3, b4, b5.
    # By tracking the contribution of each element upwards:
    # S = 5*b1 + 14*b2 + 19*b3 + 14*b4 + 5*b5

    # We search for the smallest S by iterating over possible values of b_i.
    # We use a priority queue to explore possible sums in increasing order.
    # The constraints are:
    # 1. b_i > 0 and integers.
    # 2. b1 < b5 (to break symmetry and follow "leftmost < rightmost").
    # 3. All 15 numbers in the triangle must be distinct.

    pq = []
    # Reasonable search range for b_i to find the minimum sum S.
    # With weights like 19 and 14, b_i values must be small.
    for b3 in range(1, 10):
        for b2 in range(1, 15):
            for b4 in range(1, 15):
                for b1 in range(1, 20):
                    for b5 in range(b1 + 1, 20):
                        s = 5*b1 + 14*b2 + 19*b3 + 14*b4 + 5*b5
                        heapq.heappush(pq, (s, b1, b2, b3, b4, b5))

    # Find the first tuple that satisfies the "all 15 are distinct" constraint.
    while pq:
        s, b1, b2, b3, b4, b5 = heapq.heappop(pq)
        b = (b1, b2, b3, b4, b5)
        vals = get_triangle_values(b)
        # Check if all 15 numbers in the triangle are distinct and positive
        if len(set(vals)) == 15 and all(v > 0 for v in vals):
            return "".join(map(str, b))

print(solve())
