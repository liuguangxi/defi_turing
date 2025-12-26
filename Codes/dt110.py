def solve():
    # We solve the equation P("BB") = B(B-1) / N(N-1) = 1/2
    # This simplifies to 2B(B-1) = N(N-1)
    # Multiplying by 4 and completing the square gives: 2(2B-1)^2 - 1 = (2N-1)^2
    # Let x = 2N - 1 and y = 2B - 1. The equation is x^2 - 2y^2 = -1.
    # This is a Pell-like equation. Solutions are given by (x_k + y_k*sqrt(2)) = (1 + sqrt(2))^(2k-1).
    # Recurrence relation for x_k and y_k:
    # x_{k+1} = 3*x_k + 4*y_k
    # y_{k+1} = 2*x_k + 3*y_k

    x, y = 1, 1  # Base case (1 + sqrt(2))^1
    limit = 2 * 10**10  # Since N > 10^10, x = 2N - 1 > 2*10^10 - 1

    while x <= limit:
        # Move to the next solution of x^2 - 2y^2 = -1
        x, y = 3 * x + 4 * y, 2 * x + 3 * y

    # After the loop, x and y satisfy x^2 - 2y^2 = -1 and N = (x+1)/2 > 10^10.
    # We need the number of blue balls B = (y+1)/2.
    return (y + 1) // 2

print(solve())
