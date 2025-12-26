def sum_cubes_digits(n):
    return sum(int(d)**3 for d in str(n))

n_solutions = []
for n in range(0, 100000, 11):
    if n // 11 == sum_cubes_digits(n):
        n_solutions.append(n)

# The solutions found are [0, 6171, 7722, 8316]
# The sum of these numbers is 0 + 6171 + 7722 + 8316 = 22209
print(n_solutions)
print(sum(n_solutions))
