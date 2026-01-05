import numpy as np
from scipy.optimize import brentq

# Perpendicular widths of the terrain regions
# Based on AB = 100 leagues, swamp width 50, and swamp orientation SW-NE (45 degrees)
# Total displacement in the direction perpendicular to the boundaries: Delta_u = 100 / sqrt(2) = 50 * sqrt(2)
# Distance from A to the first swamp shore: (50 * sqrt(2) - 50) / 2 = 25 * sqrt(2) - 25
u_segments = [25 * np.sqrt(2) - 25, 10, 10, 10, 10, 10, 25 * np.sqrt(2) - 25]
velocities = [10, 9, 8, 7, 6, 5, 10]

# Required lateral displacement parallel to boundaries to go from A to B: Delta_w = 100 / sqrt(2) = 50 * sqrt(2)
dw_target = 50 * np.sqrt(2)

# Snell's Law: sin(theta) / v = k. Displacement is sum of u_i * tan(theta_i)
def g(k):
    return sum(u * (k * v) / np.sqrt(1 - (k * v)**2) for u, v in zip(u_segments, velocities)) - dw_target

# Solve for the optimal Snell constant k (refractive constant)
k_opt = brentq(g, 0, 1/10 - 1e-12)

# Total travel time: T = sum( u_i / (v_i * cos(theta_i)) )
total_time = sum(u / (v * np.sqrt(1 - (k_opt * v)**2)) for u, v in zip(u_segments, velocities))

# Output time rounded to 10 decimal places with the decimal point omitted
print(f"total_time = {total_time}")
print(f"{total_time:.10f}".replace(".", ""))
