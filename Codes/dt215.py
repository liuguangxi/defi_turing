import numpy as np
from scipy.optimize import fsolve

def solve_mystery_triangle():
    """
    Solves for the 'mystery' triangle which is a fixed point of the vertex
    reflection transformation. For a triangle with angles A, B, C and sides
    a, b, c, the reflected triangle's sides satisfy:
    a'^2 = b^2 + c^2 - 2bc cos(3A)
    b'^2 = c^2 + a^2 - 2ca cos(3B)
    c'^2 = a^2 + b^2 - 2ab cos(3C)

    Similarity A'B'C' ~ ABC requires the ratios a'^2/b^2, b'^2/c^2, c'^2/a^2
    to be equal to a constant k^2.
    """

    def equations(vars):
        A_deg, B_deg = vars
        A, B = np.radians(A_deg), np.radians(B_deg)
        C = np.pi - A - B

        # Sides proportional to sines of angles
        a, b, c = np.sin(A), np.sin(B), np.sin(C)

        # Ratios derived from side lengths of the reflected triangle
        # For the mystery triangle, the permutation is (a'/b)^2 = (b'/c)^2 = (c'/a)^2
        r1 = (b**2 + c**2 - 2*b*c*np.cos(3*A)) / b**2
        r2 = (c**2 + a**2 - 2*c*a*np.cos(3*B)) / c**2
        r3 = (a**2 + b**2 - 2*a*b*np.cos(3*C)) / a**2

        return [r1 - r2, r2 - r3]

    # Initial guess based on search for obtuse fixed point
    initial_guess = [17.0, 32.1]
    sol = fsolve(equations, initial_guess, xtol=1e-12)

    # Sort acute angles
    angles = sorted([sol[0], sol[1]])

    # Round to 10^-5 (5 decimal places) as per instructions
    a1 = round(angles[0], 5)
    a2 = round(angles[1], 5)
    print(f"a1 = {a1}, a2 = {a2}")

    # Calculate exact product of these two approximate values
    product = a1 * a2

    # Format result: product omitting the decimal point
    result = str(product).replace('.', '')
    # Note: result usually expected to be the decimal-stripped string.
    # 17.02726 * 32.13231 = 547.1251967706
    return result

print(solve_mystery_triangle())
